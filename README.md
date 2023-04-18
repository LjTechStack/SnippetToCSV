# SnippetToCSV

This is a Python script that converts Alfred snippets to CSV files. The script processes all JSON and Plist files found
under the given folder and generates two CSV files: "snippet.csv" and "snippet_extra.csv".

The "snippet.csv" file contains the basic information about the Alfred snippets: name, keyword, snippet code, and the
folder name. The "snippet_extra.csv" file contains the additional information about the snippets, such as the prefix and
suffix for the keyword, and the folder name.

The script first defines the header and formats for the CSV files, then initializes two empty lists: SNIPPET_LIST
and SNIPPET_EXTRA_LIST, which will be filled with the snippet data.

The main logic of the script is in the walk_through_folder() function, which walks through all files under the given
folder and processes the JSON and Plist files by calling the corresponding processing functions: process_json_files()
and process_plist_files(). These functions extract the required data from the JSON and Plist files and create the
corresponding CSV lines using the create_snippet_data() and create_snippet_extra_data() functions.

Finally, the script writes the generated CSV data to files using the write() function. The output files are placed under
the "output" folder, which is created if it doesn't exist.

The script takes the folder path to process as an argument from the command line. It then calls the
walk_through_folder() function and writes the generated CSV data to files.