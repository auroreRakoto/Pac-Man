from mlx import Mlx
from datas import WindowInfo

def mymouse(button, x, y, mystuff):
    print(f"Got mouse event! button {button} at {x},{y}.")

def mykey(keynum, mystuff):
    print(f"Got key {keynum}, and got my stuff back:")
    print(mystuff)
    if keynum == 32:
        m.mlx_mouse_hook(win_ptr, None, None)
    if keynum == 65307:
        m.mlx_mouse_hook(win_ptr, None, None)

def gere_close(dummy):
    m.mlx_loop_exit(mlx_ptr)

def create_window() -> None:
    menuWindow = WindowInfo("menu Window", 200, 200)
    win_ptr = m.mlx_new_window(mlx_ptr, menuWindow.size_x, menuWindow.size_y, menuWindow.title)
    m.mlx_clear_window(mlx_ptr, win_ptr)
    m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Hello PyMlx!")
    (ret, w, h) = m.mlx_get_screen_size(mlx_ptr)
    print(f"Got screen size: {w} x {h} .")

    stuff = [1, 2]
    m.mlx_mouse_hook(win_ptr, mymouse, None)
    m.mlx_key_hook(win_ptr, mykey, stuff)
    m.mlx_hook(win_ptr, 33, 0, gere_close, None)

    m.mlx_loop(mlx_ptr)

def run_loop():
    pass

m = Mlx()
mlx_ptr = m.mlx_init()
create_window()

run_loop()