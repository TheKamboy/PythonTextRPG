from languages.english import LANGUAGE as english

_LANGUAGE_LIST = [english]

def load_language(index:int) -> dict:
    if index > len(_LANGUAGE_LIST)-1:
        print("ERROR: ID is not valid!")
        exit(1)

    return _LANGUAGE_LIST[index]

def amount_of_languages_in_list() -> int:
    """For language selector."""
    return len(_LANGUAGE_LIST)