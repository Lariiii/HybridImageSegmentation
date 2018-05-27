from dataPreprocessing import pruning
from read_files import *
import numpy
from PIL import Image

def dataframePreprocessing(dataframe):
    min_x = 1000000
    max_x = 0
    min_y = 1000000
    max_y = 0

    for i, row in dataframe.iterrows():
        dataframe.set_value(i, 'x', row['x'] / 100)
        dataframe.set_value(i, 'y', row['y'] / 100)
        if row['x'] < min_x:
            min_x = row['x']
        if row['x'] > max_x:
            max_x = row['x']
        if row['y'] < min_y:
            min_y = row['y']
        if row['y'] > max_y:
            max_y = row['y']

    for i, row in dataframe.iterrows():
        dataframe.set_value(i, 'x', row['x'] - min_x)
        dataframe.set_value(i, 'y', row['y'] - min_y)

    return dataframe

def dataframeToImage(dataframe, filename):
    #ToDO: Make Jannik Happy
    classRangeHigh = 0
    for i, row in dataframe.iterrows():
        if int(row['class']) > classRangeHigh:
            classRangeHigh = int(row['class'])

    # Not True in general, but for this PoC
    if classRangeHigh > 42:
        continuous = True
    elif classRangeHigh == 1:
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
