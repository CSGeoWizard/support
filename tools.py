import tkinter as tk
from tkinter import simpledialog
import json


TITLE = "Update JSON File"
PROMPT = "What city were you born in?"
JSON_FILE = "config_test.json"
JSON_KEY = "city"
DEFAULT_KWLIST = ["SS-26","bmp","S-400","SS-N-30","TOS-1A","kh-101","kh-102","SA-17","SA-27","SS-NX-33",
                            "Shahed-136","Shahed-236","Geran-2","Zoopark","rocket","ukraine","elon"]


def create_empty_json(json_file):
    blank_search = []

    file = open(json_file, "r")
    json_object = json.load(file)
    file.close()

    # overwrite the current value in the json file with input data
    file = open(json_file, "w")
    json_object['twitter']['search_list'] = blank_search
    json_object['telegram']['search_list'] = blank_search
    # json_object[json_key] = new_value
    json.dump(json_object, file, indent=4)
    file.close()


def popup(popup_title, popup_prompt):
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    user_input = simpledialog.askstring(title=popup_title, prompt=popup_prompt)
    
    return user_input


def modify_twitter_json(json_file, keys=['type', 'start_date', 'end_date', 'search', 'n_tweets', 'kwList'], values=[]):
    """
    json_file: JSON File to modify
    twitter_val: index value in the JSON file
    keys: dictionary containing [type, start_date, end_date, search, n_tweets, kwList]
    values: dictionary containing new values for keys
    """
    new_search = {keys[0]: values[0], keys[1]: values[1], keys[2]: values[2], keys[3]: values[3],
                                  keys[4]: values[4], keys[5]: values[5]}

    # open and load json file
    file = open(json_file, "r")
    json_object = json.load(file)
    file.close()

    # overwrite the current value in the json file with input data
    file = open(json_file, "w")
    # json_object[json_key] = new_value
    json_object['twitter']['search_list'].append(new_search)
    json.dump(json_object, file, indent=4)
    file.close()


def modify_telegram_json(json_file, keys=['channel', 'kwList'], values=[]):
    """
    json_file: JSON File to modify
    twitter_val: index value in the JSON file
    keys: dictionary containing [channel, kwList]
    values: dictionary containing new values for keys
    """
    new_search = {keys[0]: values[0], keys[1]: values[1], keys[2]: values[2]}

    # open and load json file
    file = open(json_file, "r")
    json_object = json.load(file)
    file.close()

    # overwrite the current value in the json file with input data
    file = open(json_file, "w")
    # json_object[json_key] = new_value
    json_object['telegram']['search_list'].append(new_search)
    json.dump(json_object, file, indent=4)
    file.close()

    
if __name__ == "__main__":
    modify_twitter_json('config_nb.json', values=['trying', 'it', 'with', 'dash', 'now', 'boy'])