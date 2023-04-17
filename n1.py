import os
import sys
folder = '9_1'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.jpg', '.png')
    output = os.rename(infilename, newname)