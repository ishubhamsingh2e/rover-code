import os
import sys
import time
from sys import platform

if __name__ == "__main__":
    _lists = sys.argv
    _inputs = _lists[2:]
    _filename = _lists[1]
    path = _inputs[0]
    listimg = []

    for files in os.listdir(path):
        if files.endswith(".jpg"):
            listimg.append(str(path+files))

    strofimg = ' '.join(map(str, listimg))
    start = time.time()

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system(f"python3 Stitch.py {strofimg}")
    elif platform == "win32":
        os.system(f"python Stitch.py {strofimg}")
    else:
        print("not a valide OS")

    end = time.time()
    with open(f"logs/{_filename}.csv", 'a') as f:
        f.write(f"{end-start}\n")
