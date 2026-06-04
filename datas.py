from dataclasses import dataclass


@dataclass
class WindowInfo:
    """Class for keeping track of the windows informations."""
    title: str
    size_x: int
    size_y: int

    def __init__(self, title: str, size_x: int, size_y: int) -> None:
        self.title = title
        self.size_x = size_x
        self.size_y = size_y


@dataclass
class Minilib:
    pass


@dataclass
class Button:
    text: str
    size_x: int
    size_y: int
    border_size_x: int
    border_size_y: int

    def __init__(
        self, text: str,
        size_x: int, size_y: int, border_size_x: int,
        border_size_y: int
    ) -> None:
        self.text = text
        self.size_x = size_x
        self.size_y = size_y
        self.border_size_x = border_size_x
        self.border_size_y = border_size_y
