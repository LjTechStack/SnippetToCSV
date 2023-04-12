"""Module convert CSV files to alfred snippets."""

import json
import os
import plistlib
import sys

SNIPPET_HEADER = "name,keyword,snippet,folder\n"
SNIPPET_EXTRA_HEADER = "snippetkeywordprefix,snippetkeywordsuffix,folder\n"
SNIPPET_LIST = []
SNIPPET_EXTRA_LIST = []


def create_snippet_data(content, folder_name):
    """create the snippet csv data from alfred."""
    snippet_line_list = [str(content["alfredsnippet"]["name"].strip()),
                         str(content["alfredsnippet"]["keyword"].strip()),
                         str(content["alfredsnippet"]["snippet"].strip()),
                         folder_name]
    return ",".join(snippet_line_list)


def create_snippet_extra_data(content, folder_name):
    """create the snippet csv data from alfred."""
    snippet_extra_line_list = [str(content["snippetkeywordprefix"].strip()),
                               str(content["snippetkeywordsuffix"].strip()),
                               folder_name]
    return ",".join(snippet_extra_line_list)


def process_json_files(root, file):
    """process json data."""
    folder_name = str(root).split("/")[-1:].pop()
    with open(os.path.join(root, file), encoding="utf8") as json_file:
        content = json.load(json_file)
        SNIPPET_LIST.append(create_snippet_data(content, folder_name))


def process_plist_files(root, file):
    """process plist data."""
    folder_name = str(root).split("/")[-1:].pop()
    with open(os.path.join(root, file), "rb") as plist_file:
        content = plistlib.load(plist_file)
        SNIPPET_EXTRA_LIST.append(create_snippet_extra_data(content, folder_name))


def walk_through_folder(folders):
    """walk through all file under the 'snippet' folder."""
    for (root, path, files) in os.walk(folders):
        for file in files:
            if str(file).endswith(".json"):
                process_json_files(root, file)
            if str(file).endswith(".plist"):
                process_plist_files(root, file)


def write(snippet_data, header, file_name):
    """write to corresponding files."""
    root = "output"
    if not os.path.isdir(root):
        os.mkdir(root)
    with open(file_name, "w", encoding="utf8") as output:
        output.write(header)
        for line in snippet_data:
            output.write(line)
            output.write("\n")


if __name__ == '__main__':
    args = sys.argv
    walk_through_folder(args[1])
    write(SNIPPET_LIST, SNIPPET_HEADER, "output/snippet.csv")
    write(SNIPPET_EXTRA_LIST, SNIPPET_EXTRA_HEADER, "output/snippet_extra.csv")
