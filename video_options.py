import keyboard
import time
from colorama import Fore, init

init()

def start(start_key: str):
    print(f"\n-> Press {start_key} to playing the video")
    while not keyboard.is_pressed(start_key.lower()):
        time.sleep(0.1)

def change_video_color(color: str):
    colors = {
    "green": Fore.GREEN,
    "red": Fore.RED,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
    "black": Fore.BLACK,
    "reset": Fore.RESET
    }

    try:
        print(colors[color.lower()])
    except KeyError:
        print(f"The color {color} don't exist, please, enter a valid color:\n {colors.keys()}", end="\n")