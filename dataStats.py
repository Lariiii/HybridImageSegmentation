from datafiles import getAllData

def getMinMax(col):
    minimum = col.min()
    maximum = col.max()
    diff = maximum - minimum
    return (minimum, maximum, diff)

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