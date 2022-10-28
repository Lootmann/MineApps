import socket

# The server's hostname or IP address
# The port used by the server
HOST, PORT = "127.0.0.1", 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # send to server
    s.sendall(b"Hello, world")
    data = s.recv(1024)


print(f"Received {data!r}")
