import json


def read_md(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found.")
        return None


def read_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{file_path}' contains invalid JSON.")
        return None


def save_md(content, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as error:
        print(f"Error saving Markdown file: {error}")


def save_json(data, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as error:
        print(f"Error saving JSON file: {error}")