from pathlib import Path
import os

a = Path("c:/Users/Millie/Desktop")

todo = []
dirs_with_jpgs = []


for curdir, sdrs, fils in os.walk(a):
    #print(fils)
    for f in fils:
        fn, ex = os.path.splitext(f)
        print (ex)
    
        

