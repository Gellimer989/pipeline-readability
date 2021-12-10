from utils import remove_comments


def avg_number(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]
    lines = remove_comments(lines)
    tot = 0
    for line in lines:
        for c in line:
            if c.isdigit():
                tot += 1

    return tot / len(lines) if tot != 0 else 0


def max_number(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]
    lines = remove_comments(lines)

    max_number = list()

    for line in lines:
        number = 0
        for c in line:
            if c.isdigit():
                number += 1
        max_number.append(number)

    return max(max_number) if max_number else 0
