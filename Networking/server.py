import argparse
import sys
import struct
import socket


# vars
INT_SIZE = 4
BUFFER_SIZE = 1024


def _form_format(data: bytes) -> str:
    '''
    Format the string format for unpacking a struct.
    '''

    data_len = len(data[INT_SIZE:])
    return f'<i{data_len}s'


def run_server(server_ip: str, server_port: int):
    '''
    Initialize a server in address (server_ip, server_port).
    '''

    server_socket = socket.socket()
    server_socket.bind((server_ip, server_port))

    while True:
        server_socket.listen()
        print("Server is up and running")

        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(BUFFER)
        length, message = struct.unpack(_form_format(data), data)
        print(f"Received data: {message.decode()}")

        client_socket.close()


def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the servers ip')
    parser.add_argument('server_port', type=int,
                        help='the servers port')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    run_server(args.server_ip, args.server_port)


if __name__ == '__main__':
    main()
