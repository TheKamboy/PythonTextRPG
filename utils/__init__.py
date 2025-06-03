from rich.console import Console
import time

import utils.npc

def typewriter(string, speed=0.003, end="\n"):
    console = Console(no_color=True)
    for char in string:
        console.print(char, end="")
        time.sleep(speed)
    print("", end=end)