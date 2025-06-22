import argparse
import sys
import struct
import socket
import threading


# vars
INT_SIZE = 4
BUFFER_SIZE = 1024


def form_format_encode(data: bytes) -> str:
    """
    Format the string format for unpacking a struct.
    """

    data_len = len(data[INT_SIZE:])
    return f'<i{data_len}s'


def thread_act(client_socket: socket) -> None:
    """
    Receive connection data in a different thread.
    """

    data = client_socket.recv(BUFFER_SIZE)
    length, message = struct.unpack(form_format_encode(data), data)
    print(f"Received data: {message.decode()}")

    client_socket.close()


def run_server(server_ip: str, server_port: int) -> None:
    """
    Initialize a server in address (server_ip, server_port).
    """

    server_socket = socket.socket()
    server_socket.bind((server_ip, server_port))

    while True:
        server_socket.listen()
        print("Server is up and running!")

        client_socket, client_address = server_socket.accept()

        curr_thread = threading.Thread(target=thread_act, args=(client_socket,))
        curr_thread.start()


def get_args() -> argparse.Namespace:
    """
    Function to get cmd arguments.
    """

    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the servers ip')
    parser.add_argument('server_port', type=int,
                        help='the servers port')
    return parser.parse_args()


def main() -> None:
    """
    Implementation of CLI and sending data to server.
    """

    args = get_args()
    run_server(args.server_ip, args.server_port)


if __name__ == '__main__':
    main()
