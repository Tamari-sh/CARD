import argparse
import sys
import struct
import socket
from typing import Tuple


###########################################################
####################### YOUR CODE #########################
###########################################################


def _form_format( data_len: int) -> str:
    '''
    Format the string format for a struct.
    '''

    return f'<i{data_len}s'


def send_data(server_ip: str, server_port: int, data: str):
    '''
    Send data to server in address (server_ip, server_port).
    '''

    client_socket = socket.socket()
    client_socket.connect((server_ip, server_port))

    data_len = len(data)
    bin_str = data.encode()
    format = _form_format(data_len)

    message = struct.pack(format, data_len, bin_str)
    client_socket.send(message.encode())

    client_socket.close()


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the servers ip')
    parser.add_argument('server_port', type=int,
                        help='the servers port')
    parser.add_argument('data', type=str,
                        help='the data')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        send_data(args.server_ip, args.server_port, args.data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
