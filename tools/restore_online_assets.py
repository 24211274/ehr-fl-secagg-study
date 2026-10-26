"""Restore verified research packages into a new directory; never starts study jobs."""
from pathlib import Path,PurePosixPath
from zipfile import ZipFile
import argparse,hashlib,json,stat
import importlib.util

# Isolated Python (-I) omits this script's directory from the module search path.
_verifier_path=Path(__file__).resolve().with_name('verify_online_assets.py')
_verifier_spec=importlib.util.spec_from_file_location('_study_online_asset_verifier',_verifier_path)
if _verifier_spec is None or _verifier_spec.loader is None:
 raise ImportError('Cannot load the script-local online asset verifier')
_verifier=importlib.util.module_from_spec(_verifier_spec)
_verifier_spec.loader.exec_module(_verifier)
digest=_verifier.digest

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--directory',type=Path,required=True)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args()
 if args.output.exists():raise ValueError('Output already exists; choose a new empty destination')
 root=Path(__file__).resolve().parents[1]
 manifest=json.loads((root/'evidence/ONLINE_RELEASE_ASSETS.json').read_text(encoding='utf-8'))
 seen=set();members=[]
 for asset in manifest['assets']:
  source=args.directory/asset['name']
  if not source.is_file() or source.stat().st_size!=asset['bytes'] or digest(source)!=asset['sha256']:
   raise ValueError('Missing or changed package: '+asset['name'])
  with ZipFile(source) as z:
   for item in z.infolist():
    name=PurePosixPath(item.filename)
    if name.is_absolute() or '..' in name.parts or '\\' in item.filename or ':' in item.filename:
     raise ValueError('Unsafe archive path')
    if stat.S_ISLNK(item.external_attr>>16):raise ValueError('Symlink archive entries are not supported')
    if item.is_dir():continue
    if item.filename in seen:raise ValueError('Cross-package collision: '+item.filename)
    seen.add(item.filename);members.append(item.filename)
   if z.testzip() is not None:raise ValueError('Archive CRC failed: '+asset['name'])
 args.output.mkdir(parents=True,exist_ok=False)
 for asset in manifest['assets']:
  with ZipFile(args.directory/asset['name']) as z:z.extractall(args.output)
 verified=0
 for path in args.output.glob('PACKAGE_MANIFEST_*.json'):
  package=json.loads(path.read_text(encoding='utf-8'))
  for row in package['files']:
   target=args.output/row['path']
   if target.stat().st_size!=row['bytes'] or digest(target)!=row['sha256']:
    raise ValueError('Restored member mismatch: '+row['path'])
   verified+=1
 result={'status':'RESTORED_AND_VERIFIED','files':len(members),'manifested_payload_files':verified,'output':str(args.output.resolve()),'training_performed':False,'historical_paths_automatically_rewritten':False}
 print(json.dumps(result,indent=2))

if __name__=='__main__':main()
