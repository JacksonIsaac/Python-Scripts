import os
from fnmatch import fnmatch
import shutil

path = os.getcwd()
dir = os.listdir(path)


for file in dir:
    if fnmatch(file, '*.py'): continue
    command = "SetFile -d \"$(GetFileInfo -m " + file + ")\" " + file
    print command
    type(command)
    print "Before"
    os.system("GetFileInfo " + file)
    os.system(command)
    print "After"
    os.system("GetFileInfo " + file)
