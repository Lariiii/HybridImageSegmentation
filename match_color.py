import cv2
import numpy
from PIL import Image

from get_shapes import edgeDetection, findContoursCV, drawContoursCV
from read_files import read_subjective2, read_subjective1

filename = 'results/testColor.png'

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

def dataframeToImageColorMerge(dataframe1, dataframe2, filename):
    classRangeHigh = 0
    for i, row in dataframe1.iterrows():
        if int(row['class']) > classRangeHigh:
            classRangeHigh = int(row['class'])

    dataframe1 = dataframePreprocessing(dataframe1)
    dataframe2 = dataframePreprocessing(dataframe2)

    im2 = cv2.imread('results/subjective1.png')
    edges2 = edgeDetection(im2)

    data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)
    data = edges2

    for i in range(len(dataframe1)):
        df1_class = dataframe1.iloc[i]['class']
        df2_class = dataframe2.iloc[i]['class']

        if df1_class == df2_class:
            print()
            data[int(dataframe1.iloc[i]['x'])][int(dataframe1.iloc[i]['y'])] = 255

    image = Image.fromarray(data)
    image.save(filename)

dataframeToImageColorMerge(read_subjective1(), read_subjective2(), filename)


#edges2 = edgeDetection(im2)
#image2, contours2, hierarchy2 = findContoursCV(edges2)
#drawContoursCV(image2, contours2, hierarchy2)