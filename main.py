from mlx import Mlx

from enum import Enum
from dataclasses import dataclass

from datas import WindowInfo, Button, Coord


class ButtonState(Enum):
    NORMAL = 1
    SELECTED = 2
    CLICKED = 3


@dataclass
class UIData:
    buttons_list: list[Button]


class Menu:
    def __init__(self):
        self.menu_window = WindowInfo("Menu Window", 500, 400)
        # self.start_button = Button("Start Game", 100, 50, 10, 10)
        # self.options_button = Button("Options", 100, 50, 10, 70)
        # self.exit_button = Button("Exit", 100, 50, 10, 130)
        pass


class Game:
    def __init__(self):
        self.game_window = WindowInfo("Game Window", 800, 600)


class Display:
    def __init__(self, menu: Menu, game: Game) -> None:
        self.mlx = Mlx()
        self.mlx_ptr = self.mlx.mlx_init()
        self.win_ptr = None
        self.menu = menu
        self.game = game

    def draw_button(self, button: Button):
        x = button.start_coords.x
        y = button.start_coords.y
        self.mlx.mlx_pixel_put(self.mlx_ptr, self.win_ptr, x, y, 255)
        print(f"Drawing button '{button.text}' at {x},{y} with size {x}x{y}.")
        self.mlx.mlx_string_put(
            self.mlx_ptr, self.win_ptr, x, y, 255, button.text
        )


def button_handler(ui: UIData, mouse: Coord) -> None:
    # print(ui)
    # print(type(ui.buttons_list))
    # print(ui.buttons_list)
    for button in ui.buttons_list:
        if mouse.is_in(button.start_coords, button.end_coords):
            print(f"on target: {button.text}")


def mymouse(button, x: int, y: int, mystuff: UIData):
    print(f"Got mouse event! button {button} at {x},{y}.")
    # print(f"mouse : {mystuff}")
    button_handler(mystuff, Coord(x, y))


def mykey(keynum, mystuff: UIData):
    print(f"Got key {keynum}, and got my stuff back:")
    # print(f"keyboard : {mystuff}")
    if keynum == 32:
        m.mlx_mouse_hook(win_ptr, None, None)
    if keynum == 65307:
        m.mlx_loop_exit(mlx_ptr)


def gere_close(dummy):
    m.mlx_loop_exit(mlx_ptr)


def draw_normal_button(button: Button):
    x = button.start_coords.x
    y = button.start_coords.y
    col = 0xFFAAAAAA

    for i in range(x, x + button.size_x):
        for j in range(y, y + button.size_y):
            m.mlx_pixel_put(mlx_ptr, win_ptr, i, j, col)
    text_x = int((x + button.size_x) * 2 / 3)
    text_y = int(y + (button.size_y / 3))
    m.mlx_string_put(mlx_ptr, win_ptr, text_x, text_y, 255, button.text)


def draw_selected_button(coord_x: int, coord_y: int, button: Button):
    for i in range(coord_x, coord_x + button1.size_x):
        for j in range(coord_x, coord_y + button1.size_y):
            col = 0xFFAAAAAA
            m.mlx_pixel_put(mlx_ptr, win_ptr, i, j, col)
    text_x = int((coord_x + button1.size_x) * 2 / 3)
    text_y = int(coord_y + (button1.size_y / 3))
    m.mlx_string_put(mlx_ptr, win_ptr, text_x, text_y, 255, button1.text)


def create_window(ui_data: UIData) -> None:
    m.mlx_clear_window(mlx_ptr, win_ptr)
    m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Pac-Man in creation")
    (ret, w, h) = m.mlx_get_screen_size(mlx_ptr)
    print(f"Got screen size: {w} x {h} .")
    for button in ui_data.buttons_list:
        draw_normal_button(button)

    stuff = UIData([button1])
    m.mlx_mouse_hook(win_ptr, mymouse, ui_data)
    m.mlx_key_hook(win_ptr, mykey, stuff)
    m.mlx_hook(win_ptr, 33, 0, gere_close, None)

    m.mlx_loop(mlx_ptr)


def run_loop():
    pass


m = Mlx()
menu = Menu()
game = Game()
display = Display(menu, game)
mlx_ptr = m.mlx_init()
menuWindow = menu.menu_window
win_ptr = m.mlx_new_window(
    mlx_ptr, menuWindow.size_x, menuWindow.size_y, menuWindow.title
)
button1 = Button("Start Game", Coord(200, 200), 120, 50, 10, 10)
button2 = Button("Options", Coord(200, 260), 120, 50, 10, 10)
button3 = Button("Exit", Coord(200, 320), 120, 50, 10, 10)

ui_data = UIData([button1, button2, button3])

create_window(ui_data)
run_loop()
