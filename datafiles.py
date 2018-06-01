from read_files import *

data_cache = None

names = [
    'corine',
    'subjective1',
    'subjective2',
    'slope',
    'aspect1',
    'aspect2',
    'aspect_degree',
    'dem',
    'ndvi'
]


def getAllData():
    """
    Read all known data sources.

    :return: Array of tuples (name, data), one for each data source
    """
    global data_cache
    if data_cache is None:
        data_cache = [
            ('corine', read_corine()),
            ('subjective1', read_subjective1()),
            ('subjective2', read_subjective2()),
            ('slope', read_slope()),
            ('aspect1', read_aspect1()),
            ('aspect2', read_aspect2()),
            ('aspect_degree', read_aspect_degree()),
            ('dem', read_dem()),
            ('ndvi', read_ndvi())
        ]
    return data_cache


def removeCoordinates(df):
    """
    Drop the coordinate columns of the dataframe
    :param df: pandas dataframe with 'x' and 'y' column
    :return: pandas dataframe without 'x' and 'y' column
    """
    return df.drop(['x', 'y'], axis=1)
