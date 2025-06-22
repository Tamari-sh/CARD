from __future__ import annotations
import argparse
import sys
import struct
import socket
from connection import *


def form_format_client(data_len: int) -> str:
    """
    Format the string format for a struct.
    """

    return f'<i{data_len}s'


def send_data(server_ip: str, server_port: int, data: str):
    """
    Send data to server in address (server_ip, server_port).
    """

    with Connection.connect_method(server_ip, server_port) as client_socket:
        bin_data = data.encode()
        client_socket.send_message(bin_data)


def get_args() -> argparse.Namespace:
    """
    Function to get cmd arguments.
    """

    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the servers ip')
    parser.add_argument('server_port', type=int,
                        help='the servers port')
    parser.add_argument('data', type=str,
                        help='the data')
    return parser.parse_args()


def main() -> None:
    """
    Implementation of CLI and sending data to server.
    """

    args = get_args()
    send_data(args.server_ip, args.server_port, args.data)
    print('Done sending data.')


if __name__ == '__main__':
    main()
