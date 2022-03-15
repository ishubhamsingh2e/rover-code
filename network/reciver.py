import socket
import tqdm
import json
import os

with open("network/metadata/default.json", "r") as _fileDefault:
    defaults = json.load(_fileDefault)
    SEPARATOR = defaults["SEPARATOR"]
    BUFFER_SIZE = defaults["BUFFER_SIZE"]
    PORT = defaults["PORT"]
    MNOQC = defaults["MNOQC"]

with open("network/metadata/reciver.json", "r") as _fileReceiver:
    reciver = json.load(_fileReceiver)
    SERVER_HOST = reciver["SERVER_HOST"]

sock = socket.socket()

sock.bind((SERVER_HOST, PORT))
sock.listen(MNOQC)
print(f"[*] Listening as {SERVER_HOST}:{PORT}")

client_socket, address = sock.accept()
print(f"[+] {address} is connected.")

received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

filename = os.path.basename(filename)

filesize = int(filesize)
progress = tqdm.tqdm(range(
    filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "wb") as f:
    while True:
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:
            break
        f.write(bytes_read)
        progress.update(len(bytes_read))

client_socket.close()
sock.close()