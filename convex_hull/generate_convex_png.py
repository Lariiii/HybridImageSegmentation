import pandas as pd
import matplotlib.pyplot as plt
import numpy
from dataPreprocessing import pruning
from PIL import Image

def dataframePreprocessing(dataframe):
    min_x = 1000000
    max_x = 0
    min_y = 1000000
    max_y = 0

    for i, row in dataframe.iterrows():
        dataframe.set_value(i, 'x', row['x'] / 100)
        dataframe.set_value(i, 'y', row['y'] / 100)
        if row['x']/100 < min_x:
            min_x = row['x']/100
        if row['x']/100 > max_x:
            max_x = row['x']/100

        if row['y']/100 < min_y:
            min_y = row['y']/100
        if row['y']/100 > max_y:
            max_y = row['y']/100

    for i, row in dataframe.iterrows():
        dataframe.set_value(i, 'x', row['x'] - min_x)
        dataframe.set_value(i, 'y', row['y'] - min_y)

    return dataframe

def dataframeToImage(dataframe, filename):
    classRangeHigh = 0
    for i, row in dataframe.iterrows():
        if int(row['class']) > classRangeHigh:
            classRangeHigh = int(row['class'])

    # Not True in general, but for this PoC
    if classRangeHigh > 42:
        continuous = True
    else:
        continuous = False

    dataframe = dataframePreprocessing(dataframe)

    data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)

    colors = []
    if continuous:
        for i, row in dataframe.iterrows():
            data[int(row['x'])][int(row['y'])] = [int((row['class'] / classRangeHigh) * 255), 0, 128]
    else:
        for i in range(classRangeHigh):
            colors.append([numpy.random.randint(low=0, high=255), numpy.random.randint(low=0, high=255),
                           numpy.random.randint(low=0, high=255)])

        for i, row in dataframe.iterrows():
            # print(""+str(row['x'])+" "+str(row['y']))
            data[int(row['x'])][int(row['y'])] = colors[int(row['class']) - 1]

    image = Image.fromarray(data)
    image.save(filename)
data = pd.read_csv('output.txt', sep=" ", header=None)
data.plot.scatter(x=0, y=1, c=2,colormap='jet')
plt.show()
data = data.drop(3,1)
data.columns = ['x','y','class']
dataframeToImage(data, 'output.png')
