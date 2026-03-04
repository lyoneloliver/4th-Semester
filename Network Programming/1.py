import socket
HOST = "a.nafkhan.id"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    response = s.recv(4096).decode()
    print(response)

    request = "5025241145"
    s.sendall(request.encode())

    response = s.recv(4096).decode()
    print(response)