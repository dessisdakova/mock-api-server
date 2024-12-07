import json
from pathlib import Path
import os

def load_test_data(filename, key=None, return_path=False):
    """Load test data from a file in the 'data' folder or return the file path"""
    data_dir = Path(__file__).resolve().parent.parent / "data"
    file_path = data_dir / filename
    
    if return_path:
        return str(file_path)

    if file_path.suffix == ".json":
        with open(file_path, 'r', encoding="utf-8") as file:
            # to prevent encoding issues for special character in database
            data = json.load(file)
        return data if key is None else data[key]

"""
def load_test_data(filename, key=None, return_path=False):
    \"""Load test data from a file in the 'data' folder or return the file path\"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    data_dir = os.path.join(parent_dir, "data")
    file_path = os.path.join(data_dir, filename)
    
    if return_path:
        return file_path
    
    _, file_extension = os.path.splitext(filename)
    if file_extension == ".json":
        with open(file_path, 'r', encoding="utf-8") as file:
            # to prevent encoding issues for special character in database
            data = json.load(file)
        return data if key is None else data[key]
"""