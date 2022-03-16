import socket
import tqdm
import json
import os

with open("network/metadata/default.json", "r") as _file:
    defaults = json.load(_file)
    SEPARATOR = defaults["SEPARATOR"]
    BUFFER_SIZE = defaults["BUFFER_SIZE"]
    port = defaults["PORT"]
    MNOQC = defaults["MNOQC"]
    HOST = defaults["HOST"]


host = HOST

filename = "test/sample_4/1.jpg"
filesize = os.path.getsize(filename)

sock = socket.socket()
print(f"[+] Connecting to {host}:{port}")
sock.connect((host, port))
print("[+] Connected.")
sock.send(f"{filename}{SEPARATOR}{filesize}".encode())

progress = tqdm.tqdm(range(
    filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        sock.sendall(bytes_read)
        progress.update(len(bytes_read))
sock.close()
