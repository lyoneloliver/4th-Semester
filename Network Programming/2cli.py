import socket

HOST = "a.nafkhan.id"
PORT = 3000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        message = input(":")
        
        pesan_final = message + "\n"
        
        s.sendall(pesan_final.encode())
        
        data = s.recv(1024)
        if not data:
            print("Server memutus koneksi (Timeout/Error).")
        else:
            print(f"Received: {data.decode()}")

except KeyboardInterrupt:
    print("\nConnection closed by user.")
except Exception as e:
    print(f"\nError: {e}")
    
# 5025241145 bore.pub:11525