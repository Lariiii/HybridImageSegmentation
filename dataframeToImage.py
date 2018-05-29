from dataPreprocessing import pruning
from read_files import *
import numpy
from PIL import Image

def dataframePreprocessing(dataframe):
    # Setting Values to find the max and min values
    min_x = 1000000
    max_x = 0
    min_y = 1000000
    max_y = 0
    
    # Make the Values smaller by dividing by 100 (since all coordinates are a multiple of 100)
    # Find Mínd and Max Values to normalize the coorindate into pixels correctly
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

    # Normalize the coordainates
    for i, row in dataframe.iterrows():
        dataframe.set_value(i, 'x', row['x'] - min_x)
        dataframe.set_value(i, 'y', row['y'] - min_y)

    return dataframe

def dataframeToImage(dataframe, filename):
    #Take a raw dataframe and build an image from that
    
    # Find the highest value the "class" field can have
    classRangeHigh = 0
    for i, row in dataframe.iterrows():
        if int(row['class']) > classRangeHigh:
            classRangeHigh = int(row['class'])

    # This checks wether you have a value range over 42 which means we will render it in some scale rather than categorical coloring
    # This is also valid if the class range goes from 0 to 1
    # The Numbers here are not true in general, but sufficient for this PoC
    if classRangeHigh > 42:
        continuous = True
    elif classRangeHigh == 1:
        continuous = True
    else:
        continuous = False
    
    # Now we will preprocess the data
    dataframe = dataframePreprocessing(dataframe)

    # Create an empty image with RGB in the dimensions of the given data
    # ToDO: Find these values from the data to generialize this approach
    data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)
    
    # Generate a random color for each class within the data or create a continous color
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

    # Generate the image from the data and save the image
    image = Image.fromarray(data)
    image.save(filename)
