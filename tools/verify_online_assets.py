"""Verify downloaded online research assets. Does not import study/model code."""
from pathlib import Path
from zipfile import ZipFile
import argparse,hashlib,json

def digest(path):
 result=hashlib.sha256()
 with path.open('rb') as stream:
  for block in iter(lambda:stream.read(1024*1024),b''):result.update(block)
 return result.hexdigest()

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--directory',type=Path,required=True)
 parser.add_argument('--require-all',action='store_true')
 args=parser.parse_args()
 root=Path(__file__).resolve().parents[1]
 manifest=json.loads((root/'evidence/ONLINE_RELEASE_ASSETS.json').read_text(encoding='utf-8'))
 checked=[];missing=[]
 for row in manifest['assets']:
  name=row['name']
  if Path(name).name!=name:raise ValueError('Unsafe asset name')
  path=args.directory/name
  if not path.is_file():missing.append(name);continue
  if path.stat().st_size!=row['bytes'] or digest(path)!=row['sha256']:
   raise ValueError('Asset bytes or SHA-256 differ: '+name)
  with ZipFile(path) as z:
   for member in z.namelist():
    if member.startswith(('/','\\')) or '..' in member.replace('\\','/').split('/'):
     raise ValueError('Unsafe archive member: '+name)
   if z.testzip() is not None:raise ValueError('Archive CRC failed: '+name)
  checked.append(name)
 if args.require_all and missing:raise ValueError('Missing release assets: '+', '.join(missing))
 if not checked:raise ValueError('No release assets found')
 print(json.dumps({'status':'PASS','verified':checked,'missing':missing,'training_performed':False},indent=2))

if __name__=='__main__':main()
