import json
import argparse
from .converter import json_to_toon, toon_to_json


def json_to_toon(json_data):
    """
    Convert JSON data to TOON format.

    :param json_data: A JSON object or a JSON-formatted string.
    :return: TOON-encoded string.
    """
    if isinstance(json_data, str):
        json_data = json.loads(json_data)  # Parse JSON string to a Python object

    return toon.encode(json_data)


def toon_to_json(toon_data):
    """
    Convert TOON data to JSON format.

    :param toon_data: A TOON-encoded string.
    :return: The decoded JSON object.
    """
    return toon.decode(toon_data)


def main():
    parser = argparse.ArgumentParser(description="Convert JSON to TOON and TOON to JSON.")
    parser.add_argument("action", choices=["json-to-toon", "toon-to-json"], help="Action to perform.")
    parser.add_argument("input", help="Input data (JSON or TOON string).")
    parser.add_argument("-o", "--output", help="Output file to save the result.", default=None)

    args = parser.parse_args()

    if args.action == "json-to-toon":
        try:
            if args.input.endswith(".json"):
                with open(args.input, "r") as file:
                    json_data = json.load(file)
            else:
                json_data = json.loads(args.input)

            result = json_to_toon(json_data)
            print("Converted TOON data:", result)

            if args.output:
                with open(args.output, "w") as file:
                    file.write(result)

        except Exception as e:
            print(f"Error converting JSON to TOON: {e}")

    elif args.action == "toon-to-json":
        try:
            result = toon_to_json(args.input)
            print("Converted JSON data:", json.dumps(result, indent=4))

            if args.output:
                with open(args.output, "w") as file:
                    json.dump(result, file, indent=4)

        except Exception as e:
            print(f"Error converting TOON to JSON: {e}")