from collections import Counter
from utils import remove_comments


def max_occurences_character(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines if line.rstrip() != ""]

    lines = remove_comments(lines)

    to_find = " ".join(lines)
    return Counter(to_find).most_common()[0][1] if lines else 0
