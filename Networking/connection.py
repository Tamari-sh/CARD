from client import *
from server import *
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


def main() -> None:
    """
    Implementation of Connection class.
    """

    pass


if __name__ == '__main__':
    main()
