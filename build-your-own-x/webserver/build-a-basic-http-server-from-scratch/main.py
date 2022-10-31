import socket

HOST = "127.0.0.1"
PORT = 8888


def parse(request: str) -> str:
    headers = request.split("\n")
    method, filename, version = headers[0].split()
    print(f"HEADER: (method, filename, version) = ({method}, {filename}, {version})")
    print(f"HOST = {headers[1]}")
    print()

    # routing
    if filename == "/":
        return "/index.html"

    return filename


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)

        print(f"Listening on PORT: {PORT}")
        print(f"http://{HOST}:{PORT}")

        while True:
            conn, addr = s.accept()

            request = conn.recv(1024).decode()

            filename = parse(request)

            try:
                fin = open(f"./{filename}")
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\n\n" + content
            except FileNotFoundError:
                response = "HTTP/1.1 404 NOT FOUND\n\nFile Not Found"

            conn.sendall(response.encode())
            conn.close()


if __name__ == "__main__":
    main()
