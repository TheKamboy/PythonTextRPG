import os
import pickle

SAVE_DATA_FILE = "game_save.pkl"
SAVE_DATA_FOLDER = "_saves"

SAVE_DATA_BASE = {
    "LANGUAGE": -69,  ## pull from languages package
    "SAVE_FILE": {},  ## pull from player data
    "SAVES": [],
}


def save_data(data):
    with open(SAVE_DATA_FILE, "wb") as f:  # open a text file
        pickle.dump(data, f)  # serialize the list
    f.close()


def create_save_folder():
    directory_name = SAVE_DATA_FOLDER
    try:
        os.mkdir(directory_name)
    except PermissionError:
        print(
            f"ERROR: Was not able to create the saves folder due to permissions. Make sure you have write access to the game folder!"
        )
        exit(1)
    except Exception as e:
        print(
            f"ERROR: Was not able to create the saves folder for the following reason: {e}"
        )
        exit(1)

    with open(f"{SAVE_DATA_FOLDER}/README.txt", "w") as f:
        f.write(
            "This is the save data folder. Do not delete this folder if you have save data in here!"
        )
    f.close()


def load_data(file=SAVE_DATA_FILE) -> dict:
    with open(file, "rb") as f:
        save = dict(pickle.load(f))
    f.close()

    return save
