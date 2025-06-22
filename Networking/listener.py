import struct
from typing import Any


class Listener:
    """Class for creating Listener"""

    def __init__(self, host: str, port: int, backlog: int = 1000) -> None:
        """Initialize the Listener class"""
        self.host = host
        self.port = port
        self.backlog = backlog

    def __repr__(self) -> str:
        """Create class representation"""
        return f"<Listener(port={self.port}, host={self.host}, backlog={self.backlog})>"


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
