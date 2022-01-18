import pandas as pd
import csv
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def init_csv():
    global BASE_PATH

    header = ['Delta', 'Loc', 'AvgAssignment', 'AvgBlankLines', 'AvgColon', 'AvgComment', 'AvgDash',
              'AvgEnvLenght', 'AvgEnvVariable', 'AvgIfStatement', 'AvgIndentation', 'AvgKeyword',
              'AvgLineLenght', 'AvgNumber', 'AvgParenthesis', 'AvgScriptLenght', 'AvgSpace', 'MaxEnvLenght',
              'MaxEnvVariable', 'MaxIndentation', 'MaxLineeLenght', 'MaxNumber', 'MaxOccurencesCharacter',
              'MaxOccurrencesEnv', 'MaxScriptLenght']  # , 'Readable'
    with open(BASE_PATH + '/../../data/dataset/metricFinal.csv', 'w', encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)


def do_sub(metric, index, df):
    return df[metric].get(index) - df[metric].get(index + 1)


def main():
    init_csv()
    df_pipeline = pd.read_csv(BASE_PATH + '/../../data/dataset/datasetFinal.csv')

    for index, row in df_pipeline.iterrows():
        csv_row = list()
        if index %2 == 0:
            name = str(df_pipeline['FileName'].get(index)) + " => " + str(df_pipeline['FileName'].get(index + 1))
            print(name)
            csv_row.append(name)
            for col in df_pipeline.columns:
                if col != 'FileName':
                    print(col)
                    csv_row.append(do_sub(str(col), index, df_pipeline))
            print(csv_row)
            with open(BASE_PATH + '/../../data/dataset/metricFinal.csv', 'a+', encoding="utf8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(csv_row)


if __name__ == '__main__':
    main()
