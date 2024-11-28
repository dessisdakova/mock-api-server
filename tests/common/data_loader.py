import json
from pathlib import Path


def load_test_data(filename, key=None, return_path=False):

    data_dir = Path(__file__).resolve().parent.parent / "data"
    file_path = data_dir / filename

    if return_path:
        return str(file_path)

    if file_path.suffix == ".json":
        with open(file_path, 'r', encoding="utf-8") as file:
            # to prevent encoding issues for special character in database
            data = json.load(file)
        return data if key is None else data[key]