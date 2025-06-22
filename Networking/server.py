from __future__ import annotations
import argparse
import sys
import struct
import socket
import threading
from listener import *


# vars
INT_SIZE = 4
BUFFER_SIZE = 1024


def form_format_server(data: bytes) -> str:
    """
    Format the string format for unpacking a struct.
    """

    data_len = len(data[INT_SIZE:])
    return f'<i{data_len}s'


def thread_act(client_connection: Connection) -> None:
    """
    Receive connection data in a different thread.
    """

    receive_msg = client_connection.receive_message()
    print(f"Received data: {receive_msg}")


def run_server(server_ip: str, server_port: int) -> None:
    """
    Initialize a server in address (server_ip, server_port).
    """

    while True:
        with Listener(server_ip, server_port) as server_socket:
            server_socket.start()
            print("Server is up and running!")
            with server_socket.accept() as client_connection:
                curr_thread = threading.Thread(target=thread_act, args=(client_connection,))
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
