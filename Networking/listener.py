import socket
import struct
from connection import *
from typing import Any


class Listener:
    """Class for creating Listener"""

    def __init__(self, host: str, port: int, backlog: int = 1000) -> None:
        """Initialize the Listener class"""
        self.host = host
        self.port = port
        self.backlog = backlog
        self.listen_socket = socket.socket()

    def __repr__(self) -> str:
        """Create class representation"""
        return f"<Listener(port={self.port}, host={self.host}, backlog={self.backlog})>"

    def __enter__(self) -> socket.socket:
        """Implement context manager __enter__ method"""
        return self.listen_socket

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Implement context manager __exit__ method"""
        stop(self)

    def start(self) -> None:
        """Start Listener listening"""

        self.listen_socket.bind((self.host, self.port))

        self.listen_socket.listen(self.backlog)

    def stop(self) -> None:
        """Close Listener Socket"""

        self.listen_socket.close()

    def accept(self) -> Connection:
        """Waits for a connection, accepts it and return a connection"""

        conn_socket, addr = self.listen_socket.accept()

        return Connection(conn_socket)


def main() -> None:
    """
    Implementation of Listener class.
    """

    with Listener(8000, '127.0.0.1') as listener:
        with listener.accept() as connection:
            print(connection)
        # connection is closed
    # listener is closed


if __name__ == '__main__':
    main()
