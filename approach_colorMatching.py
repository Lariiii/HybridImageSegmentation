import cv2
import numpy
from PIL import Image

from getContours import edgeDetection, findContoursCV, drawContoursCV
from dataframeToImage import dataframePreprocessing
from read_files import read_subjective2, read_subjective1

filename = 'results/testColor.png'

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
            data[int(dataframe1.iloc[i]['x'])][int(dataframe1.iloc[i]['y'])] = 255

    image = Image.fromarray(data)
    image.save(filename)

def run():
    dataframeToImageColorMerge(read_subjective1(), read_subjective2(), "results/colorMap.png")
