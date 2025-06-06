## Check the about_game() function (in this file) for game credits

## basic story idea:
## you arrive at a town that your friend is in, when the town is under attack.
## you have to get in sneakily to be able to save them, since you find out that he is still in there from his family.

## ## Regular Important Libraries
from rich.console import Console
from rich.prompt import Confirm, Prompt
from subprocess import call
import os
from pathlib import Path

## ## Game Libraries
## # Graphics
import graphics

## # Utilities
from utils import typewriter

## # Languages
import languages

## # Saving
import save_data

## # The game itself
import game
from game import player
from game import game_save
from game import language

console = Console()

## HELP_MSG = """[bold]HELP:[/]
## No Help Available (so leave me alone)"""


def load_save_data() -> bool:
    """Loads the game data
    (not to be confused with the load save function in the save_data module)

    :returns: Returns False if save data doesn't exist,
        and if save data doesn't have a language saved (just in case)"""
    global game_save, language
    file_location = Path(save_data.SAVE_DATA_FILE)
    save = dict

    if file_location.is_file():
        save = save_data.load_data()
    else:
        return False

    ## Nice
    if save["LANGUAGE"] == -69:
        return False

    language = languages.load_language(save["LANGUAGE"])
    game_save = save

    return True


def clear_screen():
    """You don't really need docstrings, since my ass code makes things more verbose, but I'm putting some in places anyway."""
    _ = call("clear" if os.name == "posix" else "cls")


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
    typewriter("""Placeholder Game Name:
    Designed, Programmed, and Writen by: Kamie!
    Some game design choices from      : The people in my Discord Server!

Socials:
    My Website    : https://kamies-blog.netlify.app
    Discord Server: https://discord.gg/saZqeK2m9d""")


# def color_typewriter(string, speed=0.05, end="\n"):
#     for char in string:
#         console.print(char, end="")
#         time.sleep(speed)
#     print("", end=end)


def character_generator():
    clear_screen()
    print(graphics.TITLE_SCREEN)
    typewriter(language["CHAR_GEN"]["NAME"]["QUESTION"])
    name = ""
    while True:
        name = str(console.input(">")).strip()

        if name == "":
            typewriter(f"{language['ERROR']['PREFIX']} ", end="", style="red")
            typewriter(language["ERROR"]["CHAR_GEN"]["NAME_EMPTY"])
            continue
        elif name.lower() == "help":
            typewriter(f"{language['HELP']['PREFIX']}", style="bold")
            typewriter(language["HELP"]["CHAR_GEN"]["NAME"])
            continue

        break
    clear_screen()
    print(graphics.TITLE_SCREEN)
    typewriter(language["CHAR_GEN"]["GENDER"]["QUESTION"])
    typewriter(f"1: {language['CHAR_GEN']['GENDER']['MALE']}")
    typewriter(f"2: {language['CHAR_GEN']['GENDER']['FEMALE']}")
    typewriter(f"3: {language['CHAR_GEN']['GENDER']['OTHER']}")
    gender = ""
    while True:
        gender = str(console.input(">")).strip()

        if gender == "1" or gender == "2" or gender == "3":
            break
        else:
            typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")
    clear_screen()
    print(graphics.TITLE_SCREEN)
    typewriter(language["CHAR_GEN"]["CLASS"]["QUESTION"])
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
            typewriter(f"{language['HELP']['PREFIX']}", style="bold")
            typewriter(language["HELP"]["CHAR_GEN"]["CLASS"])
        else:
            typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")
    clear_screen()
    print(graphics.TITLE_SCREEN)
    ## this whole section looks like ass, i know
    typewriter(language["CHAR_GEN"]["CONFIRM"]["TO_CONFIRM"], end="")
    typewriter(language["CHAR_GEN"]["CONFIRM"]["DOT_DOT_DOT"], speed=0.5)
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['NAME']} {name}")
    selected_gender = ""
    if gender == "1":
        selected_gender = language["CHAR_GEN"]["GENDER"]["MALE"]
    elif gender == "2":
        selected_gender = language["CHAR_GEN"]["GENDER"]["FEMALE"]
    elif gender == "3":
        selected_gender = language["CHAR_GEN"]["GENDER"]["OTHER"]
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['GENDER']} {selected_gender}")
    selected_class = ""
    if charclass == "1":
        selected_class = language["CHAR_GEN"]["CLASS"]["SWORDSMAN"]
    elif charclass == "2":
        selected_class = language["CHAR_GEN"]["CLASS"]["RANGER"]
    elif charclass == "3":
        selected_class = language["CHAR_GEN"]["CLASS"]["WIZARD"]
    elif charclass == "4":
        selected_class = language["CHAR_GEN"]["CLASS"]["ALL-ROUNDER"]
    typewriter(f"{language['CHAR_GEN']['CONFIRM']['CLASS']} {selected_class}")
    typewriter(language["CHAR_GEN"]["CONFIRM"]["DOT_DOT_DOT"], speed=0.5, end="")
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

        typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
        typewriter(f" {language['ERROR']['NOT_OPTION']}")

    if confirm == "y":
        print("unfished")
        exit(1)
    else:
        character_generator()


## Checks if the main menu hasn't been loaded yet.
## If it hasn't, then it prints the title screen with typewriter(), otherwise it uses print()
main_menu_first_load_check_yes_why_am_i_making_this_name_long = False


def new_or_load_game():
    print(graphics.TITLE_SCREEN)
    typewriter(language["MAIN_MENU"]["START_GAME_SUB"]["NEW_OR_LOAD_QUESTION"])
    typewriter(f"1: {language['MAIN_MENU']['START_GAME_SUB']['NEW_GAME']}")
    typewriter(f"2: {language['MAIN_MENU']['START_GAME_SUB']['LOAD_GAME']}")
    typewriter(f"3: {language['MAIN_MENU']['START_GAME_SUB']['GO_BACK']}")
    ask = ""
    while True:
        ask = str(console.input(">")).lower().strip()

        if ask == "1" or ask == "2" or ask == "3":
            break
        elif ask == "back":  ## fix muscle memory issues
            ask = "3"
            break
        elif ask == "help":
            ## those who know: skull
            typewriter(f"{language['HELP']['PREFIX']}", style="bold")
            typewriter(language["HELP"]["MAIN_MENU"])
        else:
            typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")

    if ask == "1":
        clear_screen()
        character_generator()
    elif ask == "2":
        print("unfished")
        exit(1)
    elif ask == "3":
        clear_screen()
        main_menu()


def main_menu():
    global main_menu_first_load_check_yes_why_am_i_making_this_name_long
    if not main_menu_first_load_check_yes_why_am_i_making_this_name_long:
        typewriter(graphics.TITLE_SCREEN)
        main_menu_first_load_check_yes_why_am_i_making_this_name_long = True
    else:
        print(graphics.TITLE_SCREEN)
    typewriter(f"1: {language['MAIN_MENU']['OPTION_1']}", end="")
    # console.print(
    #     "[black not bold](v0.0.0 \[pre-alpha])[/]"
    # )  ## i hate that it keeps complaining here about "\["
    typewriter("(v0.0.0 [pre-alpha])", style="black not bold")
    typewriter(f"2: {language['MAIN_MENU']['OPTION_2']}")
    typewriter(f"3: {language['MAIN_MENU']['OPTION_3']}")
    ask = ""
    while True:
        ask = str(console.input(">")).lower().strip()

        if ask == "1" or ask == "2" or ask == "3":
            if ask != "2":
                break
            else:
                about_game()
        elif ask == "exit":  ## fix muscle memory issues
            ask = "3"
            break
        elif ask == "help":
            ## those who know: skull
            typewriter(f"{language['HELP']['PREFIX']}", style="bold")
            typewriter(language["HELP"]["MAIN_MENU"])
        elif ask == "debug":
            if game.DEBUG_MODE:
                pass
            else:
                typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
                typewriter(f" {language['ERROR']['NOT_OPTION']}")
        else:
            typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
            typewriter(f" {language['ERROR']['NOT_OPTION']}")

    if ask == "1":
        clear_screen()
        new_or_load_game()
    elif ask == "2":
        pass
    elif ask == "3":
        typewriter(language["OTHER"]["EXIT_MSG"])
        exit(0)


def language_selector():
    global language
    lang_index = 0
    typewriter("What language do you want to use?")
    for index in range(languages.amount_of_languages_in_list()):
        index_plus_1 = index + 1
        temp_lang = languages.load_language(index)
        typewriter(f"{index_plus_1}: {temp_lang['NAME']}")

    ask = ""
    while True:
        ask = str(console.input(">")).lower().strip()

        ask_int = 0
        if ask.isdigit():
            ask_int = int(ask)

        if languages.amount_of_languages_in_list() >= ask_int > 0:
            lang_index = ask_int - 1
            language = languages.load_language(lang_index)
            break

        typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
        typewriter(f" {language['ERROR']['NOT_OPTION']}")

    game_save["LANGUAGE"] = lang_index
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
