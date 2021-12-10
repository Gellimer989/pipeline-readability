from assignments import avg_assignment
from blank_lines import avg_blank_lines
from colon import avg_colon
from comments import avg_comment
from dashes import avg_dash
from env_variables import avg_env_variable, max_env_lenght, max_env_variable, max_occurrences_env, avg_env_lenght
from if_statement import avg_if_statement
from indentation import avg_indentation, max_indentation
from keywords import avg_keyword
from line_length import avg_line_lenght, max_linee_lenght
from calc_numbers import avg_number
from parenthesis import avg_parenthesis
from scripts_lenght import avg_script_lenght, max_script_lenght
from spaces import avg_space
from calc_numbers import max_number
from occurences_character import max_occurences_character
from utils import lines_of_codes, take_redable
import csv
import os



def main():
    init_csv()

    for filename in os.listdir('D:\Desktop\Legibilita\pipeline'):
        print("n° " + filename)

        write_csv('pipeline/' + str(filename) )



def init_csv():
    header = ['FileName', 'Loc', 'AvgAssignment', 'AvgBlankLines', 'AvgColon', 'AvgComment', 'AvgDash',
              'AvgEnvLenght', 'AvgEnvVariable', 'AvgIfStatement', 'AvgIndentation', 'AvgKeyword',
              'AvgLineLenght', 'AvgNumber', 'AvgParenthesis', 'AvgScriptLenght', 'AvgSpace', 'MaxEnvLenght',
              'MaxEnvVariable', 'MaxIndentation', 'MaxLineeLenght', 'MaxNumber', 'MaxOccurencesCharacter',
              'MaxOccurrencesEnv', 'MaxScriptLenght', 'Redable']
    with open('dataset/dataset.csv', 'w', encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(header)


def write_csv(file_name):
    row_data = [file_name, lines_of_codes(file_name), avg_assignment(file_name), avg_blank_lines(file_name),
                avg_colon(file_name),
                avg_comment(file_name), avg_dash(file_name), avg_env_lenght(file_name), avg_env_variable(file_name),
                avg_if_statement(file_name), avg_indentation(file_name), avg_keyword(file_name),
                avg_line_lenght(file_name), avg_number(file_name), avg_parenthesis(file_name),
                avg_script_lenght(file_name), avg_space(file_name), max_env_lenght(file_name),
                max_env_variable(file_name), max_indentation(file_name), max_linee_lenght(file_name),
                max_number(file_name), max_occurences_character(file_name),
                max_occurrences_env(file_name), max_script_lenght(file_name),take_redable(file_name)]
    with open('dataset/dataset.csv', 'a+', encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(row_data)


if __name__ == '__main__':
    main()
