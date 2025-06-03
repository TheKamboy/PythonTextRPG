import pickle

SAVE_DATA_FILE = "game_save.pkl"

SAVE_DATA_BASE = {
    "LANGUAGE": {}, ## pull from languages package
    "SAVE_FILE": {}, ## pull from player data
}

def save_data(data):
    with open(SAVE_DATA_FILE, 'wb') as f:  # open a text file
        pickle.dump(data, f)  # serialize the list
    f.close()

def load_data() -> dict:
    with (open(SAVE_DATA_FILE, 'rb') as f):
        save = dict(pickle.load(f))
    f.close()

    return save