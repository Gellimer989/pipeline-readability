from utils import clean_env_list, find_env_variable, remove_from_quotes, lines_of_codes
import re


def avg_env_lenght(filename):
    env_list = clean_env_list(find_env_variable(filename))
    tot_len = 0
    if env_list:
        for var in env_list:
            tot_len = tot_len + len(var)
        return tot_len / len(env_list)
    else:
        return 0


def avg_env_variable(filename):
    env_list = find_env_variable(filename)
    tot_var = 0

    for var in env_list:
        var = var.replace(":", "=")
        tot_var = tot_var + len(var.split("=")) - 1

    return tot_var / lines_of_codes(filename) if tot_var != 0 else 0


def max_env_lenght(filename):
    env_list = clean_env_list(find_env_variable(filename))
    return len(max(env_list, key=len)) if env_list else 0


def max_env_variable(filename):
    env_list = find_env_variable(filename)

    max_env = list()

    for var in env_list:
        var = remove_from_quotes(var)
        var = var.replace(":", "=")
        max_env.append(len(var.split("=")) - 1)
    if max_env:
        return max(max_env)
    else:
        return 0


def max_occurrences_env(filename):
    env_list = clean_env_list(find_env_variable(filename))
    with open(filename, encoding="utf8") as file:
        lines = file.readlines()
        lines = [line.strip().replace(" ", "") for line in lines]

    to_find = " ".join(lines)
    occurrncies = list()
    for var in env_list:
        if re.findall(r'\b' + var + r'\b', to_find):
            occurrncies.append(len(re.findall(r'\b' + var + r'\b', to_find)))
    return max(occurrncies) if occurrncies else 0
