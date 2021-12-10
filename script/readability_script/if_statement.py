import re
from utils import remove_comments


def avg_if_statement(filename):
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
    lines = [line.rstrip().replace("-", "") for line in lines]
    lines = remove_comments(lines)
    ifs = 0
    for line in lines:
        if re.search(r'\b' + "if" + r'\b', line):
            ifs += 1
    return ifs / len(lines) if ifs != 0 else 0
