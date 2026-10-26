"""Path-only wrapper for the unchanged saved-score arithmetic audit; no model is loaded."""
from pathlib import Path
import argparse,subprocess,sys

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--restored',type=Path,required=True)
 parser.add_argument('--output',type=Path,required=True)
 args=parser.parse_args()
 root=Path(__file__).resolve().parents[1]
 output=args.output.resolve()
 if output.exists():raise ValueError('Output exists; choose a new destination')
 if output.is_relative_to(root):raise ValueError('Choose an output directory outside the repository')
 names={'scores':'saved_scores_original.zip','report':'final_evaluation_original.zip','completion':'training_completion_original.zip','source':'frozen_source_original.zip','benchmark':'benchmark_original.zip'}
 command=[sys.executable,'-B',str(root/'analysis/final_score_audit/audit_scores.py')]
 for name,filename in names.items():
  path=args.restored.resolve()/'audit_inputs'/filename
  if not path.is_file():raise ValueError('Missing audit input: '+filename)
  command.extend(['--'+name,str(path)])
 command.extend(['--output',str(output)])
 return subprocess.run(command,check=False).returncode

if __name__=='__main__':raise SystemExit(main())
