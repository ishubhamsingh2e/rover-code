import socket
import tqdm
import json
import os


def download(client_socket, address) -> None:
    print(f"\n[+] {address}")

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)

    progress = tqdm.tqdm(
        range(filesize),
        f"Receiving {filename}",
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        ascii=False
    )

    with open(f"recived/{filename}", "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))
    print()


with open("network/metadata/default.json", "r") as _fileDefault:
    defaults = json.load(_fileDefault)
    SEPARATOR = defaults["SEPARATOR"]
    BUFFER_SIZE = defaults["BUFFER_SIZE"]
    PORT = defaults["PORT"]
    MNOQC = defaults["MNOQC"]
    SERVER_HOST = defaults["SERVER_HOST"]

sock = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

sock.setsockopt(
    socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
)

sock.bind((SERVER_HOST, PORT))
sock.listen(MNOQC)

print(f"[*] Listening as {SERVER_HOST}:{PORT}\n")

if __name__ == "__main__":
    while True:
        client_socket, address = sock.accept()
        download(client_socket, address)

    client_socket.close()
    sock.close()
