import languages
import player_stuff
import save_data
import utils

## THOSE WHO KNOW: 💀💀💀
DEBUG_MODE = True
player = player_stuff.PLAYER_BASE
game_save = save_data.SAVE_DATA_BASE
language = languages.english  ## those who default


def item_message_handler(msg_type: str, item_name: str):
    message = language["ITEM"]["MESSAGES"][msg_type]
    item_name_first_letter = item_name[:1].lower()
    a_or_an = language["ITEM"]["MESSAGES"]["HANDLING"]["A"]

    # print(item_name_first_letter)

    for val in language["ITEM"]["MESSAGES"]["HANDLING"]["LETTERS_TO_LOOK_FOR"]:
        # print(val)
        if item_name_first_letter == val:
            a_or_an = language["ITEM"]["MESSAGES"]["HANDLING"]["AN"]
            break

    message = message.replace("[an]", a_or_an)
    message = message.replace("[item]", item_name)

    utils.typewriter(message)
