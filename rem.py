import os
import glob
for srt in glob.glob("*/*_swe.srt"):
    os.remove(srt)
