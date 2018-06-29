import argparse
from pathlib import Path
import os

parser = argparse.ArgumentParser(description='switch virtual environments')

parser.add_argument('command',type=str,help='init, use')
parser.add_argument('folder',type=str,help='virtual environment directory')

parsed = parser.parse_args()

# init
if parsed.command == 'init':
  if Path(parsed.folder).exists():
    raise FileExistsError(f'{parsed.folder} exists')
  os.system(f'$PVM_PYTHON -m venv {parsed.folder}')
  exit()

# use
elif parsed.command == 'use':
  if not Path(parsed.folder).exists():
    raise FileNotFoundError(f'{parsed.folder} not found')

  activate = f'{os.path.abspath(parsed.folder)}/bin/activate'
  print(activate)
  exit()

else:
  raise Exception('invalid command')

