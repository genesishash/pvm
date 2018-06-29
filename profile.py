import sys
import os

print(f"""

#### PVM ####
export PVM_PYTHON="{sys.executable}"
export PVM_FILENAME="{os.path.dirname(os.path.realpath(__file__))}/pvm.py"
export PVM_WRAPPER="{os.path.dirname(os.path.realpath(__file__))}/wrapper"
alias pvm="source $PVM_WRAPPER $@"
#### PVM ####

""".strip())

