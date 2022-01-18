import pandas as pd
import requests
import csv
import github
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

def init_csv():
    header = ['ID', 'RepoName', 'CommitId', 'Previous', 'CommitMessage']
    with open(BASE_PATH + '/../../data/dataset/previousCommit.csv', 'w', encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)


def get_hash_parent(sha_commit, project_name):
    g = github.Github("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")
    try:
        parent = g.get_repo(project_name).get_commit(sha_commit).parents[0].sha
        print(parent)
    except:
        return None

    return parent


def write_on_csv(id, repo_name, hash, redable, commit_message):
    row_data = [id, repo_name, hash, redable, commit_message]
    with open(BASE_PATH + '/../../data/dataset/previousCommit.csv', 'a', encoding="utf8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row_data)


def get_pipeline(sha_commit, project_name):
    if sha_commit is not None:
        print(str(project_name) + '/' + str(sha_commit))
        url = 'https://raw.githubusercontent.com/' + str(project_name) + '/' + str(sha_commit) + '/.travis.yml'
        print(url)
        r = requests.get(url)
        if r.text != "404: Not Found":
            with open(BASE_PATH + '/../../data/pipeline/' + str(sha_commit) + '.yml', 'w', encoding='utf-8') as f:
                f.write(r.text)
            print(sha_commit + " done!")


def main():
    df_commit = pd.read_csv(BASE_PATH + '/../../data/dataset/manualFiltCommits.csv')
    init_csv()
    i = 0
    for index, row in df_commit.iterrows():
        commit_hash = str(row['CommitId'])
        print(commit_hash)
        project_name = row['RepoName']
        commit_parent = get_hash_parent(commit_hash, project_name)
        write_on_csv(i, project_name, commit_hash, 1, row['CommitMessage'])
        i = i + 1
        if commit_parent:
            write_on_csv(i, project_name, commit_parent, 0, " ")
            i = i + 1
    df_pipeline = pd.read_csv(BASE_PATH + '/../../data/dataset/previousCommit.csv')
    df_pipeline = df_pipeline.dropna()
    for index, row in df_pipeline.iterrows():
        get_pipeline(row['CommitId'], row['RepoName'])


if __name__ == '__main__':
    main()
