import pandas as pd
import os

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def main():
    df = pd.read_csv(BASE_PATH+'/../../data/dataset/parentCommit.csv', index_col="ID")

    # id extracted manually
    ids = [22, 28, 38, 42, 56, 90, 92, 98, 104, 110, 124, 134, 208, 212, 218, 258, 260, 296, 348, 414, 510, 524, 544,
           546, 548, 598, 678, 680, 718, 798, 902, 910, 946, 962, 978, 1014, 1028, 1036, 1066, 1126, 1128, 1336, 1528,
           1542,
           1558, 1588, 1622, 1624, 1718, 1776, 1782, 1814, 1866, 1934, 1960, 1992, 2006, 2064, 2138, 2164, 2166, 2290,
           2300,
           2310, 2318, 2322, 2346, 2376, 2438, 2500, 2504, 2524, 2528, 2530, 2536, 2630, 2636, 2638, 2704, 2764, 2766,
           2778,
           2868, 2884, 2886, 2890, 2912, 2916, 2922, 2930, 2972, 2992, 3006, 3022, 3076, 3116, 3118, 3122, 3166, 3316,
           3356,
           3358, 3360, 3402, 3450]

    rows = pd.DataFrame()

    for id in ids:
        rows = rows.append(df.loc[id])
        rows = rows.append(df.loc[id + 1])

    rows.to_csv(BASE_PATH+'/../../data/dataset/manualFiltCommits.csv', index=True)

    # exstract only CommitId
    id_pipeline = pd.read_csv(BASE_PATH+'/../../data/dataset/manualFiltCommits.csv')
    id_pipeline["CommitId"].to_csv(BASE_PATH+'/../../data/dataset/exstractedId.csv', index=False)


if __name__ == '__main__':
    main()