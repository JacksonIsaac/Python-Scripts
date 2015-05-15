import os
from fnmatch import fnmatch
import shutil

path = os.getcwd()
dir = os.walk(path)

for root, dirs, files in dir:
    for file in files:
        if fnmatch(file, '*.py') or fnmatch(file, '.*'): continue
        
        command = "SetFile -d \"$(GetFileInfo -m " + os.path.join(root, file) + ")\" " + os.path.join(root, file)
        print command
        #type(command)
        print "Before"
        os.system("GetFileInfo " + file)
        os.system(command)
        print "After"
        os.system("GetFileInfo " + file)
