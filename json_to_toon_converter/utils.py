import json

def read_json_file(file_path):
    """
    Read JSON data from a file.

    :param file_path: Path to the JSON file.
    :return: Parsed JSON object.
    """
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path, json_data):
    """
    Write JSON data to a file.

    :param file_path: Path to the output file.
    :param json_data: JSON data to write.
    """
    with open(file_path, 'w') as file:
        json.dump(json_data, file, indent=4)
