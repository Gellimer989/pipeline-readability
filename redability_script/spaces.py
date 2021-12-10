from utils import remove_comments


def avg_space(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
    lines = remove_comments(lines)
    spaces = 0
    for line in lines:
        for c in line:
            if c == " ":
                spaces += 1

    return spaces/len(lines) if spaces != 0 else 0
