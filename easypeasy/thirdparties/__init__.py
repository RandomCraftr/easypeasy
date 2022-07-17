import os
import sys
# This line enable to copy third parties source here and have their local import still working
# Each of the third party is handled as an independent python package, but packaged here for version control
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
