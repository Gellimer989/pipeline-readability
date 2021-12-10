from utils import remove_comments


def avg_parenthesis(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]
    lines = remove_comments(lines)
    tot = 0
    for line in lines:
        for c in line:
            if c == "(" or c == ")" or c == "[" or c == "]" \
                    or c == "{" or c == "}":
                tot += 1
    return tot / len(lines) if tot!= 0 else 0

