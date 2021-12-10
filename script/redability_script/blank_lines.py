def avg_blank_lines(file_name):
    with open(file_name, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]

    blank_lines = 0
    for line in lines:
        if line == "":
            blank_lines += 1

    return blank_lines / len(lines) if blank_lines != 0 else 0
