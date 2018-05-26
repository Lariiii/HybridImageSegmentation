import pandas as pd
from read_files import *
from datafiles import *

def pruning():
    dataframe = read_dem()
    df = removeCoordinates(dataframe)

    median = df.median(axis=1)
    std = df.std(axis=1)

    df = df.assign(median=median.values)
    df = df.assign(std=std.values)

    #print(df)

    temp = []

    for index, data in df.iterrows():
        ls = data.tolist()
        std = ls[-1]
        median = ls[-2]
        factor = 1
        minimum = median - factor * std
        maximum = median + factor * std
        # new = [ i for i, d in enumerate(ls[:-2]) if not (minimum <= d and d <= maximum) ]
        new = [(minimum <= d and d <= maximum) for d in ls[:-2] ]

        temp.append(new)

    for x in temp:
        #print(x)
        pass

    headers = removeCoordinates(dataframe).columns.values.tolist()
    df_new = pd.DataFrame(temp, columns=headers)
    print(df_new.head())
    matchingCounts = df_new.sum(axis=0)
    print(matchingCounts)
    bestMatch = matchingCounts.argmax()

    print(bestMatch, matchingCounts[bestMatch])
    print(matchingCounts.sort_values())

