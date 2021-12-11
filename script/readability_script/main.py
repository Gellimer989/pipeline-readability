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
from utils import lines_of_codes, take_readable
import csv
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

def main():
    global BASE_PATH
    
    init_csv()

    with open(BASE_PATH + '/../../data/dataset/dataset.csv', 'a+', encoding="utf8") as f:
        writer = csv.writer(f)
        for filename in os.listdir(BASE_PATH + "/../../data/pipeline"):
            print("Using " + filename)
            write_csv(writer, BASE_PATH + "/../../data/pipeline/" + filename)



def init_csv():
    global BASE_PATH
    
    header = ['FileName', 'Loc', 'AvgAssignment', 'AvgBlankLines', 'AvgColon', 'AvgComment', 'AvgDash',
              'AvgEnvLenght', 'AvgEnvVariable', 'AvgIfStatement', 'AvgIndentation', 'AvgKeyword',
              'AvgLineLenght', 'AvgNumber', 'AvgParenthesis', 'AvgScriptLenght', 'AvgSpace', 'MaxEnvLenght',
              'MaxEnvVariable', 'MaxIndentation', 'MaxLineeLenght', 'MaxNumber', 'MaxOccurencesCharacter',
              'MaxOccurrencesEnv', 'MaxScriptLenght', 'Readable']
    with open(BASE_PATH + '/../../data/dataset/dataset.csv', 'w', encoding="utf8") as f:
        writer = csv.writer(f)
        writer.writerow(header)


def write_csv(writer, file_name):
    global BASE_PATH
    
    row_data = [
                file_name.split("/")[-1], 
                lines_of_codes(file_name), 
                avg_assignment(file_name), 
                avg_blank_lines(file_name),
                avg_colon(file_name),
                avg_comment(file_name),
                avg_dash(file_name), 
                avg_env_lenght(file_name),
                avg_env_variable(file_name),
                avg_if_statement(file_name), 
                avg_indentation(file_name), 
                avg_keyword(file_name),
                avg_line_lenght(file_name), 
                avg_number(file_name), 
                avg_parenthesis(file_name),
                avg_script_lenght(file_name), 
                avg_space(file_name), 
                max_env_lenght(file_name),
                max_env_variable(file_name), 
                max_indentation(file_name), 
                max_linee_lenght(file_name),
                max_number(file_name), 
                max_occurences_character(file_name),
                max_occurrences_env(file_name), 
                max_script_lenght(file_name),
                take_readable(file_name, BASE_PATH + '/../../data/dataset/parentCommit.csv')
               ]
    
    writer.writerow(row_data)


if __name__ == '__main__':
    main()
