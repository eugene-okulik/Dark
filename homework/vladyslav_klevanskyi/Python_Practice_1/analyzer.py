import argparse
import os


# Initialize argument parser to handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Path to the logs folder")
parser.add_argument(
    "phrase",
    help=("Phrase for search. If a phrase consists of several words, "
          "put them in quotation marks.")
)
parser.add_argument(
    "--first",
    help="Display only the first match", action="store_true"
)
args = parser.parse_args()
path_str = args.directory
phrase = args.phrase
first = args.first


def find_phrase_context(line: str, search_phrase: str) -> str:
    """
    Finds a portion of a log line that contains the search phrase
    along with a few words before and after it for context.

    Args:
        line (str): The log line in which to search.
        search_phrase (str): The phrase to search for within the log line.

    Returns:
        str: A snippet of the log line around the found phrase for context.
    """
    # Split the line and the search phrase into words
    line_words = line.split()
    phrase_words = search_phrase.split()

    # Find the index of the first and last word of the phrase in the line
    first_word_index = line_words.index(phrase_words[0])
    last_word_index = line_words.index(phrase_words[-1])

    # Get context by including 5 words before and 5 words after the phrase
    start_index = max(0, first_word_index - 5)
    end_index = min(len(line_words), last_word_index + 6)

    # Return the snippet with the found phrase context
    return ' '.join(line_words[start_index: end_index])


def read_file(filename: str) -> tuple:
    """
    Reads a file line by line and yields each line with its line number.

    Args:
        filename (str): Path to the file to be read.

    Yields:
        tuple: Line number and the line of the file.
    """
    line_num = 0
    with open(filename, "r") as data_file:
        for line in data_file.readlines():
            line_num += 1
            yield line_num, line


def retrieve_logs(path_string, find_phrase, first_only) -> None:
    """
    Searches for a specific phrase in all the log files within a given
    directory. It prints out the matching line number, file name, and context
    of the search phrase.

    Args:
        path_string (str): Path to the directory containing the log files.
        find_phrase (str): The phrase to search for in the log files.
        first_only (bool): Whether to display only the first matching result.
    """
    # List all files in the specified directory
    filename_list = os.listdir(path_string)

    # Iterate over each file in the directory
    for file_name in filename_list:
        file_path = os.path.join(path_string, file_name)

        # Read each line from the file
        for data_line in read_file(file_path):
            line_num, line = data_line
            # Check if the phrase is found in the current line
            if phrase in line:
                # Print the file name, line number, and context of the
                # found phrase
                print(
                    "File name:",
                    file_name,
                    "Line number:",
                    line_num,
                    "Log data:",
                    find_phrase_context(line=line, search_phrase=find_phrase)
                )
                # If we only need the first match, exit after finding
                # the first match
                if first_only:
                    return


if __name__ == "__main__":
    # Call the function to retrieve logs based on the command-line arguments
    retrieve_logs(path_string=path_str, find_phrase=phrase, first_only=first)
    print("Done!")
