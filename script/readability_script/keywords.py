from utils import remove_from_quotes
from utils import remove_comments


def avg_keyword(filename):
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.replace(" ", "") for line in lines]
    lines = remove_comments(lines)
    tot_keyword = 0

    for line in lines:
        line = remove_from_quotes(line)
        if ":" in line:
            tot_keyword += 1
    return tot_keyword/len(lines) if tot_keyword != 0 else 0


