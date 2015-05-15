import os
import shutil

path = os.getcwd()
dir = os.listdir(path)


for file in dir:
  os.rename(file, file.replace("_", ""))
