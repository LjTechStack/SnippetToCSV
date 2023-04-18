"""Module convert CSV files to alfred snippets."""

import json
import os
import plistlib
import sys

FORWARD_SLASH = os.path.sep
SNIPPET_HEADER = "name,keyword,snippet,folder\n"
SNIPPET_EXTRA_HEADER = "snippetkeywordprefix,snippetkeywordsuffix,folder\n"
SNIPPET_LIST = []
SNIPPET_EXTRA_LIST = []
ALFRED_SNIPPET = "alfredsnippet"


def create_snippet_data(content, folder_name):
    """Create the snippet CSV data from an Alfred JSON snippet."""
    name = content[ALFRED_SNIPPET]["name"].strip()
    keyword = content[ALFRED_SNIPPET]["keyword"].strip()
    snippet = content[ALFRED_SNIPPET]["snippet"].strip()
    return f"{name},{keyword},{snippet},{folder_name}"


def create_snippet_extra_data(content, folder_name):
    """Create the snippet CSV data from an Alfred plist snippet."""
    prefix = content["snippetkeywordprefix"].strip()
    suffix = content["snippetkeywordsuffix"].strip()
    return f"{prefix},{suffix},{folder_name}"


def process_json_files(root, file):
    """Process an Alfred JSON snippet file."""
    folder_name = str(root).split(FORWARD_SLASH)[-1]
    with open(os.path.join(root, file), encoding="utf8") as json_file:
        content = json.load(json_file)
        SNIPPET_LIST.append(create_snippet_data(content, folder_name))


def process_plist_files(root, file):
    """Process an Alfred plist snippet file."""
    folder_name = str(root).split(FORWARD_SLASH)[-1]
    with open(os.path.join(root, file), "rb") as plist_file:
        content = plistlib.load(plist_file)
        SNIPPET_EXTRA_LIST.append(create_snippet_extra_data(content, folder_name))


def walk_through_folder(folders):
    """Walk through all files under the 'snippet' folder and process them."""
    for root, _, files in os.walk(folders):
        for file in files:
            if file.endswith(".json"):
                process_json_files(root, file)
            elif file.endswith(".plist"):
                process_plist_files(root, file)


def write(snippet_data, header, file_name):
    """Write the snippet data to a CSV file."""
    root = "output"
    os.makedirs(root, exist_ok=True)
    with open(os.path.join(root, file_name), "w", encoding="utf8") as output:
        output.write(header)
        output.writelines([f"{line}\n" for line in snippet_data])


if __name__ == '__main__':
    args = sys.argv
    walk_through_folder(args[1])
    write(SNIPPET_LIST, SNIPPET_HEADER, "snippet.csv")
    write(SNIPPET_EXTRA_LIST, SNIPPET_EXTRA_HEADER, "snippet_extra.csv")
