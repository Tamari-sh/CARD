import struct
from typing import Any


class Listener:
    """Class for creating Listener"""
    def __init__(self, host: str, port: int, backlog: int = 1000) -> None:
        """Initialize the Listener class"""
        self.host = host
        self.port = port
        self.backlog = backlog
