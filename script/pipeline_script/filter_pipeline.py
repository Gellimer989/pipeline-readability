import pandas as pd
import os
import csv

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def init_csv():
    header = ['ID', 'RepoName', 'CommitId', 'Redable', 'CommitMessage']
    with open(BASE_PATH + '/../../data/dataset/parentFiltered.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)


def filter_dataset(hash):
    filt_datatset = pd.read_csv(BASE_PATH + '/../../data/dataset/dataset.csv')
    out = pd.DataFrame()
    out = out.append(filt_datatset[filt_datatset['FileName'] == str(hash) + ".yml"], ignore_index=True)

    if not os.path.isfile(BASE_PATH + '/../../data/dataset/datasetFiltred.csv') :
        out.to_csv(BASE_PATH + '/../../data/dataset/datasetFiltred.csv', mode='w', index=False)
    else:
        out.to_csv(BASE_PATH + '/../../data/dataset/datasetFiltred.csv', mode='a', index=False, header=False)


def main():
    global BASE_PATH

    init_csv()
    filit_parent = pd.read_csv(BASE_PATH + '/../../data/dataset/parentCommit.csv')
    filit_parent = filit_parent.dropna()

    i = -1
    for row in filit_parent.iterrows():
        i = i + 1
        if str(row[1]['CommitMessage']) != " ":
            for word in str(row[1]['CommitMessage']).split(" "):
                # def the filter word for the commit message
                if word.lower().find("restructur") != -1 or word.lower().find("read") != -1  or word.lower().find("clean") != -1:
                    # save the matched row and the row[0]+1 indexes
                    row_data_1 = [row[1]['ID'], row[1]['RepoName'], row[1]['CommitId'], row[1]['Redable'],
                                  row[1]['CommitMessage']]
                    filter_dataset(row[1]['CommitId'])
                    row_data_0 = filit_parent.iloc[i + 1]
                    filter_dataset(filit_parent.iloc[i + 1]['CommitId'])
                    with open(BASE_PATH + '/../../data/dataset/-parentFiltered.csv', 'a', encoding="utf-8",
                              newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(row_data_1)
                        writer.writerow(row_data_0)
                    break


if __name__ == '__main__':
    main()
