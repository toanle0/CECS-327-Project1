import argparse
from distributed_server import DistributedServer
import logging

# Configure logging
logging.basicConfig(filename='project.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def start_server(port):
    """Initialize and run the distributed server on the given port."""
    server = DistributedServer(port=port)
    server.run()


def main():
    # Argument parsing for customization from the terminal
    parser = argparse.ArgumentParser(
        description="Start the main server for the distributed communication project.")
    parser.add_argument("--port", type=int, default=5001,
                        help="Port for the server to run on.")

    args = parser.parse_args()

    # Starting the server with specified (or default) arguments
    start_server(args.port)


if __name__ == "__main__":
    main()
