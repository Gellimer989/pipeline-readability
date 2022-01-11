import re
import pandas


def take_readable(filename, dataset):
    print(filename.split("/")[-1].split(".")[0])
    to_find = pandas.read_csv(dataset)
    to_find = to_find.dropna()
    filtred = to_find[to_find['CommitId'].str.contains(filename.split("/")[-1].split(".")[0])]
    print(filtred['Redable'].values[0])
    return filtred['Redable'].values[0]


def lines_of_codes(filename):
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
    return len(lines)


def find_avg_char(filename, char):
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip().replace(" ", "") for line in lines]
    lines = remove_comments(lines)
    tot = 0

    for line in lines:
        for c in line:
            if c == char:
                tot += 1

    return tot / len(lines) if tot != 0 else 0


def remove_comments(list):
    for i, line in enumerate(list):
        if "#" in remove_from_quotes(list[i]):
            list[i] = list[i].split('#')[0]
    return [x for x in list if x]


def count_indent(string):
    return len(string) - len(string.lstrip())


def remove_from_quotes(line):
    line = re.sub('["](.*?)["]', '', line)
    line = re.sub("['](.*?)[']", "", line)
    return line


def remove_from_parentheses(line):
    line = re.sub("([\(\[]).*?([\)\]])", "", line)
    line = re.sub("[()]", "", line)
    return line


def find_env_variable(filename):
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()

    lines = remove_comments(lines)
    env_list = list()

    i = 0
    j = 1
    for line in lines:
        if line.strip().startswith("env"):
            env_list.append(line)
            # aggiungo tutte le linee con un indentazione maggiore al di sotto del tag "env:"
            while (i + j < len(lines)) and (count_indent(lines[i + j]) > count_indent(line) or (
                    count_indent(lines[i + j]) == count_indent(line) and (lines[i + j].lstrip().startswith("-")))):
                env_list.append(lines[i + j])
                j += 1
        elif line.replace("-", "").strip().startswith("env"):
            env_list.append(lines[i])
        j = 1
        i += 1
    for k, var in enumerate(env_list):
        env_list[k] = remove_from_quotes(env_list[k].strip())
        env_list[k] = remove_from_parentheses(env_list[k])
        if env_list[k].startswith('-'):
            env_list[k] = env_list[k].split("-")[1].lstrip()
        if ":" in env_list[k]:
            if env_list[k].split(":")[1] == "":
                env_list[k] = "0"
            # per evitare casi come -> global:CAMPFIRE_TOKEN=abc123
            elif env_list[k].split(":")[0] == "env" or env_list[k].split(":")[0] == "global" or \
                    env_list[k].split(":")[0] == "jobs":
                env_list[k] = env_list[k].split(":")[1].lstrip()
        if env_list[k].startswith("*"):
            env_list[k] = env_list[k].replace("*", "")

    return [x for x in env_list if x != "0" and not x.startswith('&')]


def clean_env_list(env_list):
    cleaned_list = list()

    for var in env_list:
        i = 0
        var = var.replace(":", "=")
        var = var.replace(" = ", "=")
        var = var.replace("= ", "=")

        while i < len(var.split("=")) and var.split("=")[i].split(" "):
            if i == 0:
                cleaned_list.append(var.split("=")[i].split(" ")[0])
            elif len(var.split("=")[i].split(" ")) > 1:
                cleaned_list.append(var.split("=")[i].split(" ")[1])
            i = i + 1

    return [x for x in cleaned_list if x and x != "secure"]


def find_script(filename):
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    lines = remove_comments(lines)

    script_list = list()

    i = 0
    j = 1
    for line in lines:
        if line.strip().startswith("script") or line.strip().startswith("install") or line.strip().startswith(
                "before_install") or line.strip().startswith("before_script") or line.strip().startswith(
            "after_script") or line.strip().startswith("after_success") or line.strip().startswith("after_failure"):
            if line.split(":", 1) == False and line.split(":", 1)[1] != '':
                script_list.append(line.split(":", 1)[1])
            # aggiungo tutte le linee con un indentazione maggiore al di sotto del tag "script:" e "install:"
            while (i + j < len(lines)) and (count_indent(lines[i + j]) > count_indent(line) or (
                    count_indent(lines[i + j]) == count_indent(line) and (lines[i + j].lstrip().startswith("-")))):
                script_list.append(lines[i + j])
                j += 1
        j = 1
        i += 1

    return [x for x in script_list if "skip" not in remove_from_quotes(x)]


def clean_script_list(script_list):
    cleaned_list = list()

    for script in script_list:
        script = script.strip()
        if script.startswith("-"):
            script = script.replace("-", "", 1).strip()
        cleaned_list.append(script)
    return [x for x in cleaned_list if x]
