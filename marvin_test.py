from dataPreprocessing import pruning
from read_files import *
import numpy
from PIL import Image

def dataframeToImage(dataframe, classRangeHigh, coninuus, filename):

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

    data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)

    colors = []
    if coninuus:
        # 0 to 1 or 0 to 600
        for i, row in dataframe.iterrows():
            data[int(row['x'])][int(row['y'])] = [int((row['class'] / classRangeHigh) * 255), 0, 128]
    else:
        for i in range(classRangeHigh):
            colors.append([numpy.random.randint(low=0, high=255), numpy.random.randint(low=0, high=255),
                           numpy.random.randint(low=0, high=255)])

        for i, row in dataframe.iterrows():
            # print(""+str(row['x'])+" "+str(row['y']))
            print(int(row['class']) - 1)
            data[int(row['x'])][int(row['y'])] = colors[int(row['class']) - 1]

    image = Image.fromarray(data)
    image.save(filename)


#df_geo = pruning(read_subjective1())
#df_geo = read_subjective1()

dataframeToImage(read_subjective1(), 12, False, 'results/subjective1.png')
dataframeToImage(read_subjective2(), 12, False, 'results/subjective2.png')
dataframeToImage(read_corine(), 41, False, 'results/corine.png')

dataframeToImage(pruning(read_aspect1()), 180, True, 'results/aspect1.png')
dataframeToImage(pruning(read_aspect2()), 180, True, 'results/aspect2.png')

dataframeToImage(pruning(read_dem()), 605, True, 'results/dem.png')
dataframeToImage(pruning(read_ndvi()), 1, True, 'results/ndvi.png')
dataframeToImage(pruning(read_slope()), 56, True, 'results/slope.png')



