import cv2
import numpy
from PIL import Image

from getContours import edgeDetection, findContoursCV, drawContoursCV
from dataframeToImage import dataframePreprocessing
from read_files import read_subjective2, read_subjective1

filename = 'results/testColor.png'

def createColorMap(dataframe1, dataframe2, show):

    # Calculate the classRangeHigh
    # The classRangeHigh equals the highest measured value in the data
    # Example Data: x y value1
    # classRangeHigh = max(value1)
    classRangeHigh = 0
    for i, row in dataframe1.iterrows():
        if int(row['class']) > classRangeHigh:
            classRangeHigh = int(row['class'])

    # Preprocess the dataframes
    # This mainly causes the dataframe to be in proper coordinates
    # E.G. to convert the coordinates into a coordinate system with the origin at 0,0
    dataframe1 = dataframePreprocessing(dataframe1)
    dataframe2 = dataframePreprocessing(dataframe2)

    # Read the Shape of the Subjective1.png
    # This is used to have a Background for the color-map
    # This is also the reason the image is in greyscale, since edgeDetection creates a greyscale image
    im2 = cv2.imread('results/subjective1.png')
    edges2 = edgeDetection(im2)
    data = edges2

    # When the class labels for a certain pixel match, place a white pixel on the image
    # Otherwise, the pixel stays black (or Background Shape)
    for i in range(len(dataframe1)):
        df1_class = dataframe1.iloc[i]['class']
        df2_class = dataframe2.iloc[i]['class']

        if df1_class == df2_class:
            data[int(dataframe1.iloc[i]['x'])][int(dataframe1.iloc[i]['y'])] = 255

    # Create a real image from the array of pixels
    image = Image.fromarray(data)
    if show:
        cv2.imshow("ColorMap", numpy.asarray(image))
        cv2.waitKey(0)
    return image

def run(show):
    # Wrapper for better software quality
    # If show = True, then all image outputs will be displayed
    return createColorMap(read_subjective1(), read_subjective2(), show)
