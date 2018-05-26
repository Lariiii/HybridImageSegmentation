import pandas as pd
from datafiles import *

def pruning(dataframe, debug=False):
    df_images = removeCoordinates(dataframe)

    medians = df_images.median(axis=1)
    std_devs = df_images.std(axis=1)

    df_images = df_images.assign(median=medians.values)
    df_images = df_images.assign(std=std_devs.values)

    #print(df)

    outlier_detection_array = []

    for _, row in df_images.iterrows():
        row_list = row.tolist()
        std_dev = row_list[-1]
        median = row_list[-2]
        sigma_factor = 1.5
        minimum = median - sigma_factor * std_dev
        maximum = median + sigma_factor * std_dev
        outlying_row = [(minimum <= d and d <= maximum) for d in row_list[:-2] ]

        outlier_detection_array.append(outlying_row)

    image_headers = removeCoordinates(dataframe).columns.values.tolist()

    df_new = pd.DataFrame(outlier_detection_array, columns=image_headers)

    if debug:
        print(df_new.head())
        print()

    matchingCounts = df_new.sum(axis=0)

    if debug:
        print(matchingCounts)
        print()

    bestMatch = matchingCounts.idxmax()

    if debug: print('best:', bestMatch, 'with', matchingCounts[bestMatch])
    if debug:
        print('The others are:\n', matchingCounts.sort_values(ascending=False))
        print()

    return dataframe[['x', 'y', bestMatch]] \
        .assign(median=medians.values) \
        .assign(std_dev=std_devs.values) \
        .rename(columns={bestMatch :'pixel'})

import numpy as np

def output_as_txt(df_pruned, outputfile='output.txt'):
    np.savetxt('results/' + outputfile, df_pruned[['x', 'y', 'pixel']].values, fmt='%f')

output_as_txt(pruning(read_ndvi()), 'nvdi.txt')