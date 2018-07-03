from pathlib import Path
import os
import re

a = Path("c:/Users/Millie/Desktop")

todo = []
dirs_with_img = []
file_types = "jpg$|mov$"  #move to config


for curdir, sdrs, fils in os.walk(a):
    for f in fils:
        #fn0, ex = os.path.splitext(f)
        if re.search(file_types, f, re.IGNORECASE):
            dirs_with_img.append(f)
            break


print(len(dirs_with_img))


        
    
        
