import json
from pathlib import Path


def read_md(file_path):
    """
    Reads and returns the contents of a Markdown file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_json(file_path):
    """
    Reads and returns the contents of a JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_md(content, file_path):
    """
    Saves content to a Markdown file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def save_json(data, file_path):
    """
    Saves data to a JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def extract_business_name(source_pack):
    """
    Extracts the business name from the first line of the source pack.

    Example:
    # Ken's Bakery ---> Ken's Bakery
    """
    first_line = source_pack.split("\n")[0]

    return first_line.replace("#", "").strip()


def create_business_folders(business_name):
    """
    Creates the required folder structure for a business.
    """

    base_path = Path("data") / business_name

    folders = [
        "source_pack",
        "analysis",
        "strategy",
        "plan",
        "content",
        "content/posts",
        "content/videos",    
        "reviews",
        "logs",
    ]

    for folder in folders:
        (base_path / folder).mkdir(
            parents=True,
            exist_ok=True,
        )