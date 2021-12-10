from utils import count_indent
from utils import remove_comments


def avg_indentation(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    lines = remove_comments(lines)
    tot = 0
    for l in lines:
        if l.strip() != "":
            tot = tot + count_indent(l)
    return tot / len(lines) if tot != 0 else 0




def max_indentation(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = remove_comments(lines)

    return max(count_indent(l) for l in lines if l.strip() != "") if lines else 0

