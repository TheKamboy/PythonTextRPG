import time

from rich.console import Console

import utils.npc


def typewriter(string, speed=0.003, style="", end="\n"):
    console = Console(no_color=True if style == "" else False)
    for char in string:
        if style == "":
            console.print(char, end="")
        else:
            console.print(f"[{style}]{char}[/]", end="")
        time.sleep(speed)
    print("", end=end)
