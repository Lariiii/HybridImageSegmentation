from datafiles import getAllData, removeCoordinates


def getMinMax(col):
    minimum = col.min()
    maximum = col.max()
    diff = maximum - minimum
    return (minimum, maximum, diff)

def getMinMaxDf(dataframe, name=''):
    data = removeCoordinates(dataframe)
    print(name, data.min(axis=1).min(), ' - ', data.max(axis=1).max())

def getAllMinMaxDf():
    data = getAllData()
    for name, df in data:
        getMinMaxDf(df, name)
    print()

'''
getAllMinMaxDf()

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
    x = 'x'
    y = 'y'
    print(getMinMax(df[x]))
    print(getMinMax(df[y]))

def statAllCoordinates():
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