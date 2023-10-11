import socket

class DistributedServer:

    def __init__(self, host='', port=5000):
        self.host = host
        self.port = port
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

    def handle_client(self, client_socket):
        # Define the logic to handle incoming client connections and messages
        message = client_socket.recv(1024).decode()
        print(f"Received: {message}")

        # Send back a confirmation message
        confirmation_message = "Message received successfully!"
        client_socket.send(confirmation_message.encode())

        # Further processing, based on your protocols, can be added here
        client_socket.close()

    # def handle_client(client_socket, client_address):
    #     """
    #     Handle client connections and messages.
    #     """
    #     try:
    #         # Receive data from the client
    #         data = client_socket.recv(BUFFER_SIZE)
    #         if data:
    #             # Decode the data and print/log it
    #             message = data.decode('utf-8')
    #             print(f"Received message: {message}")
    #
    #             # Process the received data (if there's any processing to be done)
    #
    #             # Send back a confirmation message to the client
    #             confirmation_message = "Message received successfully!"
    #             client_socket.send(confirmation_message.encode())
    #
    #         else:
    #             print("Client disconnected")
    #
    #     except Exception as e:
    #         print(f"Error handling client: {e}")
    #     finally:
    #         client_socket.close()
    #
    def run(self):
        self.start()
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            self.handle_client(client_socket)


if __name__ == "__main__":
    server = DistributedServer(port=5001)
    server.run()
