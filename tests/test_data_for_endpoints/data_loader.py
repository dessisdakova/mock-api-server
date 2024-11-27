import os
import json


def load_test_data(filename, key):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the file
    file_path = os.path.join(current_dir, filename)

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data[key]