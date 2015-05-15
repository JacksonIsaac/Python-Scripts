import os
from fnmatch import fnmatch
import shutil

path = os.getcwd()
dir = os.walk(path)

# This will rename the files under the current directory and all the sub-directories
for root, dirs, files in dir:
    for file in files:
        if fnmatch(file, '*.py') or fnmatch(file, '.*'): continue
        #print "\nBefore"
        #print os.path.join(root, file)
        os.rename(os.path.join(root, file), os.path.join(root, file.replace(" ", "_")))
        #print "\nAfter"
        #print os.path.join(root, file)
