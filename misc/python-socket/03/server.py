import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    HOST, PORT = "127.0.0.1", 65432

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")

        while True:
            # get message
            data = conn.recv(1024)
            if not data:
                break
            # send to client
            conn.sendall(data)
