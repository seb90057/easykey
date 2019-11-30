"""Fichier d'installation de notre script main.py."""

from cx_Freeze import setup, Executable
import sys

path = sys.path
includes = []
excludes = []
packages = ["src",
            "src.utils",
            "src.utils.file_utils",
            "src.utils.file_utils.csv_utils",
            "src.utils.tools",
            "src.utils.tools.grouping",
            "src.utils.tools.utils",
            "src.viz",
            "src.viz.CsvFileDetails",
            "src.viz.easykey",
            "src.viz.FileKey",
            "src.viz.ScrollFrame"]

options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }

# On appelle la fonction setup
setup(
    name="easykey",
    version="0.1",
    description="Ce programme vous dit bonjour",
    executables=[Executable("main.py")],
    options={"build_exe": options},
)