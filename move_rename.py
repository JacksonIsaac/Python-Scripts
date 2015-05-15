import os
import shutil

path = os.getcwd()
dir = os.walk(path)

rem = dir.next()[1]

for file in dir:
  for files in file[2]:
    try:
      shutil.move(file[0] + os.sep + files, path)
    except shutil.Error:
      continue

for dirs in rem:
  shutil.rmtree(path + os.sep + dirs)

filenames = os.listdir(path)

for filename in filenames:
  os.rename(filename, filename.replace("_", ""))
