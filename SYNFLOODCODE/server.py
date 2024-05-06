import socket

def start_server(host='0.0.0.0', port=80):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind((host, port))
    serv_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            cl_socket, addr = serv_socket.accept()
            print(f"Accepted connection from {addr}")
            cl_socket.close()
    except KeyboardInterrupt:
        print("Shutting down server")
    finally:
        serv_socket.close()

if __name__ == "__main__":
    start_server()
