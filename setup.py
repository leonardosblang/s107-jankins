import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "excludes": ["tkinter"],
                     "build_exe": "build"}
BASE_PLATFORM = "Win32GUI" if sys.platform == "win32" else None

setup(
    name="build",
    version="1.0",
    description="Buildtests",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=None,
                            target_name="test-build.exe")],
)
