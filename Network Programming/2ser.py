import socket
import hashlib

HOST = "0.0.0.0"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(2)

    print(f"Serv running on {HOST}:{PORT}")
    while True:
        try:
            cli_sock, cli_addr = sock.accept()

            with cli_sock:
                print(f"Connected to {cli_addr}")
                while True:
                    buf = cli_sock.recv(4096)
                    if not buf:
                        break
                    print(f"Received data from client at {cli_addr}: {buf.decode()}")
                    hashed = hashlib.md5(buf).hexdigest()
                    cli_sock.sendall(hashed.encode() + b"\n")
        except KeyboardInterrupt:
            print("Server Closing")
            exit(0)
