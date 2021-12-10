from utils import clean_script_list, find_script


def avg_script_lenght(filename):
    script_list = clean_script_list(find_script(filename))

    tot_len = 0
    if script_list:
        for var in script_list:
            tot_len = tot_len + len(var)
        return tot_len / len(script_list)
    else:
        return 0


def max_script_lenght(filename):
    script_list = clean_script_list(find_script(filename))
    return len(max(script_list, key=len)) if script_list else 0
