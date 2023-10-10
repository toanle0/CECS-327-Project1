import socket
import sys

def send_message_to_server(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)

    print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python simple_client.py HOST PORT MESSAGE")
        sys.exit(1)

    host, port, message = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    send_message_to_server(host, port, message)

