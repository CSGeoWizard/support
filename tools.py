import tkinter as tk
from tkinter import simpledialog
import json


TITLE = "Update JSON File"
PROMPT = "What city were you born in?"
JSON_FILE = "config_test.json"
JSON_KEY = "city"


def popup(popup_title, popup_prompt):
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    user_input = simpledialog.askstring(title=popup_title, prompt=popup_prompt)
    
    return user_input


def modify_twitter_json(json_file, twitter_val=0, keys=['type', 'start_date', 'end_date', 'search', 'n_tweets', 'kwList'], values=[]):
    """
    json_file: JSON File to modify
    twitter_val: index value in the JSON file
    keys: dictionary containing [type, start_date, end_date, search, n_tweets, kwList]
    values: dictionary containing new values for keys
    """

    # you have to read the file to create the json object and then close it
    # then open it again in write mode because otherwise the cursor will be
    # at the end of the first file open that created the json file. Then,
    # when you try to dump new data into it, it deletes all the data before
    # the cursor and won't end up writing data because the object field
    # will be deleted.

    # open and load json file
    file = open(json_file, "r")
    json_object = json.load(file)
    file.close()

    # overwrite the current value in the json file with input data
    file = open(json_file, "w")
    # json_object[json_key] = new_value
    for i in range(len(keys)):
        json_object['twitter']['search_list'][twitter_val][keys[i]] = values[i]
        json_object['twitter']['search_list'][twitter_val][keys[i]] = values[i]
        json_object['twitter']['search_list'][twitter_val][keys[i]] = values[i]
        json_object['twitter']['search_list'][twitter_val][keys[i]] = values[i]
        json_object['twitter']['search_list'][twitter_val][keys[i]] = values[i]
        json_object['twitter']['search_list'][twitter_val][keys[i]] = values[i]
    json.dump(json_object, file, indent=4)
    file.close()


def modify_telegram_json(json_file, twitter_val=0, keys=['channel', 'kwList'], values=[]):
    """
    json_file: JSON File to modify
    twitter_val: index value in the JSON file
    keys: dictionary containing [channel, kwList]
    values: dictionary containing new values for keys
    """

    # you have to read the file to create the json object and then close it
    # then open it again in write mode because otherwise the cursor will be
    # at the end of the first file open that created the json file. Then,
    # when you try to dump new data into it, it deletes all the data before
    # the cursor and won't end up writing data because the object field
    # will be deleted.

    # open and load json file
    file = open(json_file, "r")
    json_object = json.load(file)
    file.close()

    # overwrite the current value in the json file with input data
    file = open(json_file, "w")
    # json_object[json_key] = new_value
    for i in range(len(keys)):
        json_object['telegram']['search_list'][twitter_val][keys[i]] = values[i]
        json_object['telegram']['search_list'][twitter_val][keys[i]] = values[i]
    json.dump(json_object, file, indent=4)
    file.close()

    
if __name__ == "__main__":
    modify_twitter_json('config_nb.json', values=['trying', 'it', 'with', 'dash', 'now', 'boy'])