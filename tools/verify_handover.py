#!/usr/bin/env python3
"""Read-only consistency check for the supervisor handover. Python standard library only."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import os
import stat

MANIFEST = 'evidence/HANDOVER_FILES_SHA256.json'
SOURCE = 'executed/EHR_FL_Main_Experiments_Package_v1_0_3'
SOURCE_MANIFEST_SHA = '0e4bc1175bf97a766d46aa60f02c4c891c483d3870957b3ae6ac52ea7734dc88'

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def safe_relative(name: str) -> str:
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or ':' in name or str(p) != name:
        raise ValueError('Unsafe manifest path: ' + repr(name))
    return name

def is_link(path: Path) -> bool:
    info = path.lstat()
    return path.is_symlink() or bool(getattr(info, 'st_file_attributes', 0) & 0x400)

def inventory(root: Path) -> set[str]:
    if is_link(root):
        raise ValueError('Root must not be a symlink or reparse point')
    files = set()
    for parent, dirs, names in os.walk(root, followlinks=False):
        parent = Path(parent)
        if parent == root and '.git' in dirs:
            if is_link(parent / '.git'):
                raise ValueError('Git metadata cannot be a symlink')
            dirs.remove('.git')
        for name in dirs + names:
            p = parent / name
            if is_link(p):
                raise ValueError('Symlink/reparse point is not allowed: ' + str(p))
        for name in names:
            p = parent / name
            if not stat.S_ISREG(p.stat().st_mode):
                raise ValueError('Non-regular file: ' + str(p))
            files.add(p.relative_to(root).as_posix())
    return files

def verify(root: Path) -> dict:
    root = root.absolute()
    observed = inventory(root)
    manifest = json.loads((root / MANIFEST).read_text(encoding='utf-8'))
    entries = manifest['files']
    listed = [safe_relative(row['path']) for row in entries]
    if len(listed) != len(set(listed)) or MANIFEST in listed:
        raise ValueError('Manifest contains duplicate or self entries')
    expected = set(listed) | {MANIFEST}
    if observed != expected:
        raise ValueError('File set mismatch; missing=' + repr(sorted(expected-observed)[:5]) +
                         '; extra=' + repr(sorted(observed-expected)[:5]))
    for row in entries:
        path = root / row['path']
        if path.stat().st_size != row['bytes'] or sha256(path) != row['sha256']:
            raise ValueError('Handover content mismatch: ' + row['path'])
    original = root / SOURCE / 'PACKAGE_SHA256SUMS.txt'
    if sha256(original) != SOURCE_MANIFEST_SHA:
        raise ValueError('Original source manifest identity changed')
    source_paths = set()
    for line in original.read_text(encoding='utf-8').splitlines():
        digest, relative = line.split('  ', 1)
        relative = safe_relative(relative)
        if relative in source_paths or sha256(root / SOURCE / relative) != digest:
            raise ValueError('Original source mismatch: ' + relative)
        source_paths.add(relative)
    actual_source = {p[len(SOURCE)+1:] for p in observed if p.startswith(SOURCE + '/')}
    if actual_source != source_paths | {'PACKAGE_SHA256SUMS.txt'} or len(source_paths) != 215:
        raise ValueError('Original source file set changed')
    return {'status': 'HANDOVER_FILES_VERIFIED_NO_EXPERIMENTS_RUN',
            'files': len(observed), 'original_source_files_verified': len(source_paths),
            'original_manifest_preserved': True, 'manifest_sha256': sha256(root / MANIFEST)}

if __name__ == '__main__':
    try:
        print(json.dumps(verify(Path(__file__).absolute().parents[1]), indent=2))
    except Exception as exc:
        raise SystemExit('STOP: ' + str(exc))
