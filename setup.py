import sys
from cx_Freeze import setup, Executable

setup(  name = "Nerd Manager",
        version = "0.1",
        description = "Nerdcastmanager",
        executables = [Executable("nerd_manager.py")])