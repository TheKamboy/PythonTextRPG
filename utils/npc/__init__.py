from game import player
from game import language
import utils

from rich.console import Console


class Conversation:
    """Creates a NPC Conversation
    :arg npc_name: The name of the NPC.
    :arg dialogue: The list of dialogue that the NPC gives.
    :arg response: The list of response that the Player can give as a reply (can be empty).
    """

    def __init__(self, npc_name: str, dialogue: list[str], response: list[str] = None):
        self._NPC_NAME = npc_name
        self._DIALOGUE = dialogue
        self._RESPONSE = response

    def _input_for_responses(self):
        console = Console(no_color=True)
        guh_int = 0

        for index, dialogue in enumerate(self._RESPONSE):
            utils.typewriter(f"{index+1}: {dialogue}")

        while True:
            guh = str(console.input(">")).lower().strip()

            if guh.isdigit():
                guh_int = int(guh)

            if len(self._RESPONSE) >= guh_int > 0:
                lang_index = guh_int - 1
                break

            utils.typewriter(f"{language['ERROR']['PREFIX']}", end="", style="red")
            utils.typewriter(f" {language['ERROR']['NOT_OPTION']}")

        return guh

    def start_conversation(self):
        console = Console(no_color=True)
        selected_option: str = ""
        for index, i in enumerate(self._DIALOGUE):
            utils.typewriter(f"{self._NPC_NAME}:", end="")
            utils.typewriter(f" {i}", speed=0.02)
            utils.typewriter(language["INPUT_PAUSE"], end="")
            console.input()

        if self._RESPONSE is not None:
            selected_option = str(self._input_for_responses())

        return selected_option
