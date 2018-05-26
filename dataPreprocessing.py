import pandas as pd
from datafiles import *
import numpy as np

def pruning(dataframe, debug=False, method='best'):
    df_images = removeCoordinates(dataframe)

    medians = df_images.median(axis=1)
    means = df_images.mean(axis=1)
    std_devs = df_images.std(axis=1)

    df_images = df_images.assign(median=medians.values)
    df_images = df_images.assign(mean=means.values)
    df_images = df_images.assign(std=std_devs.values)

    extra_value_count = 3

    if method == 'best':
        df_pruned = prune_to_best_image(dataframe, df_images, extra_value_count, debug)
    elif method == 'mean':
        df_pruned = prune_to_avg_image(dataframe, df_images, extra_value_count, debug)
    else:
        raise NotImplementedError

    return df_pruned.assign(median=medians.values) \
        .assign(std_dev=std_devs.values) \
        .rename(columns={'pixel' : 'class'})

# return df with [x, y, pixel]
def prune_to_best_image(dataframe, df_images, extra_value_count, debug, sigma_factor=1.5):

    outlier_detection_array = []

    for _, row in df_images.iterrows():
        row_list = row.tolist()
        std_dev = row_list[-extra_value_count + 2]
        median = row_list[-extra_value_count + 0]
        minimum = median - sigma_factor * std_dev
        maximum = median + sigma_factor * std_dev
        outlying_row = [(minimum <= d and d <= maximum) for d in row_list[:-extra_value_count]]

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
        .rename(columns={bestMatch: 'pixel'})

def prune_to_avg_image(dataframe, df_images, extra_value_count, debug):
    return dataframe[['x', 'y']].assign(pixel=df_images['mean'])

def output_as_txt(df_pruned, outputfile='output.txt'):
    np.savetxt('results/' + outputfile, df_pruned[['x', 'y', 'class']].values, fmt='%f')

output_as_txt(pruning(read_ndvi()), 'nvdi.txt')