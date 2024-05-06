import socket
from threading import Thread

def handle_client(sock, addr):
    try:
        sock.settimeout(5)  # Set a timeout for the client to respond
        data = sock.recv(1024)  # Try to receive data from client
        if data:
            print(f"Received data from {addr}")
        else:
            print(f"No response from {addr}, closing connection")
    except socket.timeout:
        print(f"Connection timeout with {addr}")
    finally:
        sock.close()

def start_server(host='192.168.4.53', port=80):
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind((host, port))
    serv_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            cl_socket, addr = serv_socket.accept()
            print(f"Accepted connection from {addr}")
            # Instead of closing the connection, handle it in a new thread
            client_thread = Thread(target=handle_client, args=(cl_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("Shutting down server")
    finally:
        serv_socket.close()

if __name__ == "__main__":
    start_server()
