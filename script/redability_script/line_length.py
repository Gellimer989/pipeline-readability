def avg_line_lenght(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]

    tot = 0
    for l in lines:
        tot = tot + len(l)

    return tot / len(lines) if tot != 0 else 0


def max_linee_lenght(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]

    return max(len(x) for x in lines) if lines else 0
