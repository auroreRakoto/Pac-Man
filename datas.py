from __future__ import annotations


from dataclasses import dataclass


@dataclass
class Coord:
    x: int
    y: int

    def __add__(self, other: Coord) -> Coord:
        res = Coord(self.x + other.x, self.y + other.y)
        return res

    def __sub__(self, other: Coord) -> Coord:
        res = Coord(self.x - other.x, self.y - other.y)
        return res

    def is_in(self, start: Coord, end: Coord) -> bool:
        if self.x < max(start.x, end.x) and self.x > min(start.x, end.x):
            if self.y < max(start.y, end.y) and self.y > min(start.y, end.y):
                return True
        return False

    def center(self, other: Coord, offset_size: Coord) -> Coord:
        x_center = ((self.x + other.x) / 2) + offset_size.x / 2
        y_center = ((self.y + other.y) / 2) + offset_size.y / 2
        res = Coord(x_center, y_center)
        return res


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
    start_coords: Coord
    size_x: int
    size_y: int
    border_size_x: int
    border_size_y: int

    def __init__(
        self,
        text: str,
        start_coords: Coord,
        size_x: int,
        size_y: int,
        border_size_x: int,
        border_size_y: int
    ) -> None:
        self.text = text
        self.start_coords = start_coords
        self.size_x = size_x
        self.size_y = size_y
        self.end_coords = start_coords + Coord(size_x, size_y)
        self.border_size_x = border_size_x
        self.border_size_y = border_size_y
