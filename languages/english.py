LANGUAGE = {
    "NAME": "English",
    "INPUT_PAUSE": "Press ENTER to continue...",
    ## ## Regular
    "HELP": {
        "PREFIX": "HELP:",
        "MAIN_MENU": "No Help Available (so leave me alone)",
        "CHAR_GEN": {
            "NAME": """Are you trying to name your character "help", or are asking for help to name your character?
If it's the other thing, maybe name your character "John", or "Jane".""",
            "GENDER": "Not sure how to help you with this one...",
            "CLASS": """Classes designed for certain weapons will have bonus damage for that weapon,
but less damage and a bigger chance of missing for weapons they're not designed for.

Swordsman   - best with melee weapons  (like swords)
Ranger      - best with ranged weapons (like bows)
Wizard      - best with magic weapons  (like staffs)
All-Rounder - good with all weapons    (no bonuses)""",
        },
    },
    "ERROR": {
        "PREFIX": "ERROR:",
        "CHAR_GEN": {"NAME_EMPTY": "Your name can't be empty!"},
        "NOT_OPTION": "Not an option.",
        "EMPTY_SAVE": "That save is empty.",
        "FALLBACK": {
            "SAVE_DELETE_BUT_SAVE_DOES_NOT_EXIST": "Weird! You tried to delete your save, but your save doesn't even exist...I'm guessing you deleted it yourself while the game was running, or the game is modified...I'll close the game anyway."
        },
    },
    ## ## In-Game Stuff
    ## ## Menus
    ## # Main Menu
    "MAIN_MENU": {
        ## Options
        "START_GAME": "Start Game   ",  ## must be 12 chars or fewer for the spacing of version number
        "SETTINGS": "Settings",
        "ABOUT": "About",
        "EXIT_GAME": "Exit Game",
        "START_GAME_SUB": {
            "NEW_OR_LOAD_QUESTION": "Would you like to start a new game, or load a saved game?",
            "NEW_GAME": "New Game",
            "LOAD_GAME": "Load Game",
        },
        "SAVE_SELECTION": {
            ## Variables
            ## - [#]: The save number.
            "QUESTIONS": {
                "LOAD_SAVE_QUESTION": "Which save would you like to load?",
                "SAVE_SAVE_QUESTION": "Which save would you like to save your progress to?",
                "DELETE_SAVE_QUESTION": "Which save would you like to delete?",
                "SHOULD_DELETE_SAVE_QUESTION": "Are you sure you want to delete Save [#]?",
            },
            "SAVE_LABEL": "Save [#]",
        },
        "SETTINGS_SUB": {
            "DELETE_SAVE": "Erase Save",
            "CHANGE_LANGUAGE": "Change Language",
            "CURRENT_LANGUAGE": "(Current Language: English)",
        },
    },
    ## # Character Generator
    "CHAR_GEN": {
        "NAME": {"QUESTION": "What will your name be?"},
        "GENDER": {
            "QUESTION": "What will your gender be?",
            "MALE": "Male",
            "FEMALE": "Female",
            "OTHER": "Other",
        },
        "CLASS": {
            "QUESTION": 'What do you want your class to be? (type "help" to learn more)',
            "SWORDSMAN": "Swordsman",
            "RANGER": "Ranger",
            "WIZARD": "Wizard",
            "ALL-ROUNDER": "All-Rounder",
        },
        "CONFIRM": {
            "TO_CONFIRM": "To confirm",
            "IS_CORRECT": "Is that correct?",
            "DOT_DOT_DOT": "...",  ## I have no clue if this will need to change between languages
            "NAME": "Your name will be:  ",
            "GENDER": "Your gender will be:",
            "CLASS": "Your class will be: ",
        },
    },
    ## # Story Messages (like actually relating to the story)
    "STORY": {"NPC": {}},
    ## # Basic NPC Dialogue (not important to the story)
    "NPC_DIALOGUE": {},
    ## # Item Names
    "ITEM": {
        "WEAPONS": {},
        "MESSAGES": {
            "HANDLING": {
                "LETTERS_TO_LOOK_FOR": ["a", "e", "i", "o", "u"],
                "A": "a",
                "AN": "an",
            },
            ## Variables:
            ## - [an]  : gets replaced with "a" or "an", depending on the starting letter of the item name. (not sure if this is used in other languages, so it is a built in thing that you can just disable by not using it)
            ## - [item]: gets replaced with the item name.
            "GOT_ITEM": "You got [an] [item]!",
            "DISCARD_ITEM": "You discarded the [item].",
        },
        "STICK": "Stick",
    },
    ## ## Other
    "OTHER": {
        "EXIT_MSG": "Goodbye!",
        "LANGUAGE_QUESTION": "",
        "DELETE_SAVE_MESSAGE": "Are you sure you want to delete your save? You will not be able to get your save back through normal means if you do.",
        "OPTIONS": {"GO_BACK": "Go Back"},
    },
}
