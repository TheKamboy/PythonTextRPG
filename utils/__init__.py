import time

from rich.console import Console


def typewriter(string, speed=0.003, style="", end="\n"):
    console = Console(no_color=True if style == "" else False)
    for char in string:
        if style == "":
            console.print(f"[not bold]{char}[/]", end="")
        else:
            console.print(f"[{style}]{char}[/]", end="")
        time.sleep(speed)
    print("", end=end)


## Couldn't think of a good name. :(
def string_with_vars_handler(string: str, var_to_look_for: str, replace: str) -> str:
    return string.replace(f"[{var_to_look_for}]", replace)
