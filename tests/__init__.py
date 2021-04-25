import os
import sys

_CURR_DIR = os.path.dirname(__file__)
_POWERLIB_DIR = os.path.abspath(os.path.join(_CURR_DIR, '..', 'src'))
sys.path.insert(0, _POWERLIB_DIR)
