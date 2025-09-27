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
        "SETTINGS_SUB": {
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
    "ITEM": {"WEAPONS": {}, "STICK": "Stick"},
    ## ## Other
    "OTHER": {
        "EXIT_MSG": "Goodbye!",
        "LANGUAGE_QUESTION": "",
        "OPTIONS": {"GO_BACK": "Go Back"},
    },
}
