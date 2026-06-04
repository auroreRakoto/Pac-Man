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
