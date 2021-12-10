from utils import remove_from_quotes


def avg_comment(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]

    tot_comments = 0
    for line in lines:
        line = remove_from_quotes(line)
        if line.find('#') != -1 or line.startswith('#'):
            tot_comments += 1

    return tot_comments / len(lines) if tot_comments != 0 else 0
