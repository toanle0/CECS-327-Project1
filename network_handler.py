import socket

class NetworkHandler:

    def __init__(self, host='', port=5000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_and_listen(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Listening on {self.host}:{self.port}")

    def accept_connection(self):
        client_socket, addr = self.socket.accept()
        return client_socket, addr

    def send(self, client_socket, message):
        client_socket.send(message.encode())

    def receive(self, client_socket, buffer_size=1024):
        return client_socket.recv(buffer_size).decode()

    def broadcast(self, message, all_nodes):
        for node in all_nodes:
            self.send(node, message)

    def anycast(self, message, optimal_node):
        self.send(optimal_node, message)

    def multicast(self, message, group_nodes):
        for node in group_nodes:
            self.send(node, message)

    def close(self, client_socket):
        client_socket.close()
