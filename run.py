import os
import sys
import time
if __name__ == "__main__":
    _lists = sys.argv
    _inputs = _lists[2:]
    _filename = _lists[1]
    path = _inputs[0]
    listimg=[]
    for files in os.listdir(path):
        if files.endswith(".jpg"):
            listimg.append(str(path+files))
    strofimg= ' '.join(map(str,listimg))
    start=time.time()
    os.system(f"python3 Stitch.py {strofimg}")
    end=time.time()
    with open(f"logs/{_filename}.csv",'a') as f:
        f.write(f"{end-start}\n")
