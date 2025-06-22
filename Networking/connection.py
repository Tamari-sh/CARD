from client import *
from server import *
import struct
from typing import Any


class Connection:
    """Class for creating connection"""

    def __init__(self, connection: socket.socket) -> None:
        """Initialize the connection class"""
        self.connection = connection

    def __repr__(self) -> str:
        """Create class representation"""
        return f"<connection from {self.connection.getpeername()} to {self.connection.getsockname()}>"

    def __enter__(self) -> socket.socket:
        """Implement context manager __enter__ method"""
        return self.connection

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Implement context manager __exit__ method"""
        self.connection.close()

    def send_message(self, message: bytes) -> None:
        """Send a message through the connection"""

        message_len = len(message)
        format = form_format_decode(message_len)

        format_message = struct.pack(format, message_len, message)
        self.connection.send(format_message)

    def receive_message(self) -> str or None:
        """Function to get a message from the connection"""

        try:
            data = self.connection.recv(BUFFER_SIZE)
            length, message = struct.unpack(form_format_encode(data), data)

            return message.decode()

        except OSError:
            print("Connection closed before data was received")

            return None


def main() -> None:
    """
    Implementation of Connection class.
    """

    pass


if __name__ == '__main__':
    main()
