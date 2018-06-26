from datafiles import getAllData, removeCoordinates

"""
Calculate some statistics on our data
"""


def getMinMax(col):
    """
    Find minimum and maximum of numbers in a column

    :param col: pandas dataframe column
    :return: minimum, maximum and span
    """
    minimum = col.min()
    maximum = col.max()
    diff = maximum - minimum
    return (minimum, maximum, diff)


def getMinMaxDf(dataframe, name=''):
    """
    Find the overall Minimum and Maximum value in a dataframe (after stripping the coordinate columns away).
    Print the results

    :param dataframe: pandas dataframe with our source data schema (two coordinate columns and the rest data values)
    :param name: (optional)
    :return: nothing (only visual printing)
    """
    data = removeCoordinates(dataframe)
    print(name, data.min(axis=1).min(), ' - ', data.max(axis=1).max())


def getAllMinMaxDf():
    """
    For all known data sources, print the min-max stats

    :return: nothing (only visual printing) - see below for our test results
    """
    data = getAllData()
    for name, df in data:
        getMinMaxDf(df, name)
    print()


'''
Result of getAllMinMaxDf()

corine 2.0  -  41.0
subjective1 1.0  -  12.0
subjective2 1.0  -  12.0
slope 0.0019213846  -  55.17975500000001
aspect1 3.5401979e-05  -  179.99971000000002
aspect2 0.00057131933  -  179.99992
aspect_degree 0.00028727295  -  359.99958
dem 52.903397  -  604.66545
ndvi 0.0  -  1.0
'''


def statCoordinates(df):
    """
    Print minimum, maximum and difference of the coordinates in the given data dataframe.
    First x is printed, then y.

    :param df: pandas data frame with our data schema
    :return: only visual
    """
    x = 'x'
    y = 'y'
    print(getMinMax(df[x]))
    print(getMinMax(df[y]))


def statAllCoordinates():
    """
    For all known data sources, print the name and min, max and diff for the x- and y-coordinate.

    :return: only visual -- see the results below
    """
    data = getAllData()
    for name, df in data:
        print(name)
        statCoordinates(df)
        print()


'''
corine
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

subjective1
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

subjective2
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

slope
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

aspect1
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

aspect2
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

aspect_degree
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

dem
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)

ndvi
(4423900.0, 4466900.0, 43000.0)
(5717100.0, 5750700.0, 33600.0)
'''
