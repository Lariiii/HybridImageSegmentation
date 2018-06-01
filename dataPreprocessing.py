import pandas as pd
from datafiles import *
import numpy as np

pruning_methods = ['best', 'mean', 'median']


def pruning(dataframe, debug=False, method='best'):
    """
    From the many images (represented by data columns in the dataframe), create one which should work as representant for
    all the others.
    You can choose the 'best' method, to keep the entity of an image. The best-fitting image will be chosen based on the
    lowest number of outliers (calculated on median and standard deviation for each pixel)
    The 'median' method will take for each image pixel the median value, so combining all images to a new one.
    Similar to the 'median', the 'mean' method will choose the average pixel value.

    :param dataframe: pandas dataframe with our data schema
    :param debug: possibility to enable additional print statements
    :param method: choose from 'best', 'mean', 'median'; define, how to find the best representant.
    :return: pandas dataframe with [x, y, class, median, std_dev]
    """
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
    elif method == 'median':
        df_pruned = prune_to_median_image(dataframe, df_images, extra_value_count, debug)
    else:
        raise NotImplementedError

    return df_pruned.assign(median=medians.values) \
        .assign(std_dev=std_devs.values) \
        .rename(columns={'pixel': 'class'})



def prune_to_best_image(dataframe, df_images, extra_value_count, debug=False, sigma_factor=1.5):
    """
    Reduce multiple image columns to one and keep the entity of an image. The best-fitting image will be chosen based on the
    lowest number of outliers (calculated on median and standard deviation for each pixel)

    :param dataframe: original dataframe with our data schema
    :param df_images: pandas df with one image per column (no coordinates)
    :param extra_value_count: specification of how many columns have manually been added to df_images
    :param debug: enable additional log messages
    :param sigma_factor: The sigma environment, which defines inliers, as a factor to the standard deviation
    :return: pandas df with [x, y, pixel]
    """
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
    """
    Reduce multiple images given as dataframe columns to the average of each pixel row

    :param dataframe: original dataframe with our data schema
    :param df_images: pandas df with one image per column (no coordinates)
    :param extra_value_count: (irrelevant) specification of how many columns have manually been added to df_images
    :param debug: (irrelevant) enable additional log messages
    :return: pandas df with [x, y, pixel]
    """
    return dataframe[['x', 'y']].assign(pixel=df_images['mean'])


def prune_to_median_image(dataframe, df_images, extra_value_count, debug):
    """
    Reduce multiple images given as dataframe columns to the average of each pixel row

    :param dataframe: original dataframe with our data schema
    :param df_images: pandas df with one image per column (no coordinates)
    :param extra_value_count: (irrelevant) specification of how many columns have manually been added to df_images
    :param debug: (irrelevant) enable additional log messages
    :return: pandas df with [x, y, pixel]
    """
    return dataframe[['x', 'y']].assign(pixel=df_images['median'])


def output_as_txt(df_pruned, outputfile='output.txt'):
    """
    Store the pruned dataframe with flow values as csv.

    :param df_pruned: pruned dataframe with [x, y, class]
    :param outputfile: destination file name
    :return: saving result
    """
    np.savetxt('results/' + outputfile, df_pruned[['x', 'y', 'class']].values, fmt='%f')


# output_as_txt(pruning(read_ndvi()), 'nvdi.txt')
