from pathlib import Path
import os
import re

a = Path("c:/Users/Millie/Desktop")
#a = Path("c:/")

todo = []
dirs_with_img = []
file_types = "jpg$|mov$"  #move to config




for curdir, sdrs, fils in os.walk(a):
    for f in fils:
        #fn0, ex = os.path.splitext(f)
        if re.search(file_types, f, re.IGNORECASE):
            dirs_with_img.append(curdir)
            break

#print(dirs_with_img)
print(len(dirs_with_img))

for pth in dirs_with_img:
    for fil in os.listdir(pth):
        f = os.path.join(pth, fil)
        if re.search(file_types, f, re.IGNORECASE):
            sz = os.stat(f)[6]
            print(fil + "  " + pth)
#            print(sz)
        
    
        
