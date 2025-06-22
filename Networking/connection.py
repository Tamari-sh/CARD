from client import *
from server import *


class Connection:
    """Class for creating connection"""

    def __init__(self, connection: socket.socket) -> None:
        """Initialize the connection class"""
        self.connection = connection

    def __repr__(self) -> str:
        """Create class representation"""
        return f"<connection from {self.connection.getpeername()} to {self.connection.getsockname()}>"


def main() -> None:
    """
    Implementation of Connection class.
    """

    pass


if __name__ == '__main__':
    main()
