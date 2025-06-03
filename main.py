## basic story idea:
## you arrive at a town that your friend is in, when the town is under attack.
## you have to get in sneakily to be able to save them, since you find out that he is still in there from his family.
import time

## ## Regular Important Libraries
import rich
from rich.console import Console
from rich.prompt import Confirm, Prompt
from subprocess import call
import os
from pathlib import Path

## ## Game Libraries
## # Graphics
import graphics

## # Defaults
import player_stuff

## # Languages
import languages

## # Saving
import save_data

console = Console()

## HELP_MSG = """[bold]HELP:[/]
## No Help Available (so leave me alone)"""

player = player_stuff.PLAYER_BASE
game_save = save_data.SAVE_DATA_BASE

language = languages.english.LANGUAGE ## those who default

def load_save_data() -> bool:
    global game_save, language
    file_location = Path(save_data.SAVE_DATA_FILE)
    save = dict

    if file_location.is_file():
        save = save_data.load_data()
    else:
        return False

    if save['LANGUAGE'] == {}:
        return False

    language = save['LANGUAGE']
    game_save = save

    return True

def clear_screen():
    _ = call('clear' if os.name == 'posix' else 'cls')

def get_player_input() -> str:
    ## Important for later
    command_requested = ""

    ## Player Input
    val = str(console.input(">")).lower().strip()

    ## Check for valid commands
    if val == "help":
        console.print(language["HELP_IN-GAME"])
    elif val == "exit":
        if Confirm.ask("Exit the game?"):
            console.print("Goodbye!")
            exit(0)
    elif val == "":
        console.print("[red]No command given.[/]")
    else:
        console.print(f"[red]Unknown command: {val}[/]")

    return command_requested

def about_game():
    ## Maybe this may change...
    typewriter(f"""Placeholder Game Name:
    Designed, Programmed, and Writen by: Kamie!
    Some game design choices from: The people in my Discord Server!

Socials:
    My Website: https://kamies-blog.netlify.app
    Discord Server: https://discord.gg/saZqeK2m9d""")

def typewriter(string, speed=0.003, end="\n"):
    console = Console(no_color=True)
    for char in string:
        console.print(char, end="")
        time.sleep(speed)
    print("", end=end)

# def color_typewriter(string, speed=0.05, end="\n"):
#     for char in string:
#         console.print(char, end="")
#         time.sleep(speed)
#     print("", end=end)

def character_generator():
    typewriter(language['CHAR_GEN']['NAME']['QUESTION'])
    name = ""
    while True:
        name = str(console.input(">")).strip()

        if name == "":
            console.print(f"[red]{language['ERROR']['PREFIX']} [/]", end="")
            typewriter(language['ERROR']['CHAR_GEN']['NAME_EMPTY'])
            continue
        elif name.lower() == "help":
            console.print(f"[bold]{language['HELP']['PREFIX']}[/]")
            typewriter(language['HELP']['CHAR_GEN']['NAME'])
            continue

        break
    typewriter(language['CHAR_GEN']['GENDER']['QUESTION'])
    typewriter(f"1: {language['CHAR_GEN']['GENDER']['MALE']}")
    typewriter(f"2: {language['CHAR_GEN']['GENDER']['FEMALE']}")
    typewriter(f"3: {language['CHAR_GEN']['GENDER']['OTHER']}")
    gender = ""
    while True:
        gender = str(console.input(">")).strip()

        if gender == "1" or gender == "2" or gender == "3":
            break
        else:
            console.print(f"[red]{language['ERROR']['PREFIX']}[/]", end="")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")

    typewriter(language['CHAR_GEN']['CLASS']['QUESTION'])
    typewriter(f"1: {language['CHAR_GEN']['CLASS']['SWORDSMAN']}")
    typewriter(f"2: {language['CHAR_GEN']['CLASS']['RANGER']}")
    typewriter(f"3: {language['CHAR_GEN']['CLASS']['WIZARD']}")
    typewriter(f"4: {language['CHAR_GEN']['CLASS']['ALL-ROUNDER']}")
    charclass = ""
    while True:
        charclass = str(console.input(">")).strip()

        if charclass == "1" or charclass == "2" or charclass == "3" or charclass == "4":
            break
        elif charclass.lower() == "help":
            console.print(f"[bold]{language['HELP']['PREFIX']}[/]")
            typewriter(language['HELP']['CHAR_GEN']['CLASS'])
        else:
            console.print(f"[red]{language['ERROR']['PREFIX']}[/]", end="")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")

    ## this whole section looks like ass, i know
    typewriter(language['CHAR_GEN']['CONFIRM']['TO_CONFIRM'], end="")
    typewriter(language['CHAR_GEN']['CONFIRM']['DOT_DOT_DOT'], speed=0.5)
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['NAME']} {name}")
    selected_gender = ""
    if gender == "1":
        selected_gender = language['CHAR_GEN']['GENDER']['MALE']
    elif gender == "2":
        selected_gender = language['CHAR_GEN']['GENDER']['FEMALE']
    elif gender == "3":
        selected_gender = language['CHAR_GEN']['GENDER']['OTHER']
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['GENDER']} {selected_gender}")
    selected_class = ""
    if charclass == "1":
        selected_class = language['CHAR_GEN']['CLASS']['SWORDSMAN']
    elif charclass == "2":
        selected_class = language['CHAR_GEN']['CLASS']['RANGER']
    elif charclass == "3":
        selected_class = language['CHAR_GEN']['CLASS']['WIZARD']
    elif charclass == "4":
        selected_class = language['CHAR_GEN']['CLASS']['ALL-ROUNDER']
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['CLASS']} {selected_class}")
    typewriter(language['CHAR_GEN']['CONFIRM']['DOT_DOT_DOT'], speed=0.5, end="")
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['IS_CORRECT']} (y/n)")
    confirm = ""
    while True:
        confirm = str(console.input(">")).strip().lower()

        if confirm == "y" or confirm == "n":
            break

        if confirm == "yes":
            confirm = "y"
            break
        elif confirm == "no":
            confirm = "n"
            break

        console.print(f"[red]{language['ERROR']['PREFIX']}[/]", end="")
        typewriter(f" {language['ERROR']['NOT_OPTION']}")

    if confirm == "y":
        print("unfished")
        exit(1)
    else:
        clear_screen()
        character_generator()


def main_menu():
    typewriter(graphics.TITLE_SCREEN)
    typewriter(f"1: {language["MAIN_MENU"]["OPTION_1"]}", end="")
    console.print("[black not bold](v0.0.0 \[pre-alpha])[/]")
    typewriter(f"2: {language["MAIN_MENU"]["OPTION_2"]}")
    typewriter(f"3: {language["MAIN_MENU"]["OPTION_3"]}")
    ask = ""
    while True:
        ask = str(console.input(">")).lower().strip()

        if ask == "1" or ask == "2" or ask == "3":
            if ask != "2":
                break
            else:
                about_game()
        elif ask == "exit": ## fix muscle memory issues
            ask = "3"
            break
        elif ask == "help":
            ## those who know: skull
            console.print(f"[bold]{language['HELP']['PREFIX']}[/]")
            typewriter(language["HELP"]["MAIN_MENU"])
        else:
            console.print(f"[red]{language['ERROR']['PREFIX']}[/]", end="")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")

    if ask == "1":
        clear_screen()
        character_generator()
    elif ask == "2":
        pass
    elif ask == "3":
        typewriter(language['OTHER']['EXIT_MSG'])
        exit(0)

def language_selector():
    global language
    typewriter("What language do you want to use?")
    typewriter("1: English")
    typewriter("2: sigma english") ## internally known as Brainrot English
    ask = ""
    while True:
        ask = str(console.input(">")).lower().strip()

        if ask == "1":
            language = languages.english.LANGUAGE
            break
        elif ask == "2":
            language = languages.brainrot_english.LANGUAGE
            break

        console.print(f"[red]{language['ERROR']['PREFIX']}[/]", end="")
        typewriter(f" {language['ERROR']['NOT_OPTION']}")

    game_save['LANGUAGE'] = language
    save_data.save_data(game_save)


def main():
    # while True:
    #     request = get_player_input()
    #     console.print(request)
    if not load_save_data():
        clear_screen()
        language_selector()
    clear_screen()
    main_menu()


if __name__ == "__main__":
    main()