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

statAllCoordinates()
