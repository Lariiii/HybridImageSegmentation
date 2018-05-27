import cv2
import numpy

from get_shapes import edgeDetection, findContoursCV, drawContoursCV

subjective_1 = cv2.imread('results/subjective1.png')
subjective_2 = cv2.imread('results/subjective2.png')

def dataframeToImageColorMerge(dataframe1, dataframe2, classRangeHigh, coninuus, filename):

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



#edges2 = edgeDetection(im2)
#image2, contours2, hierarchy2 = findContoursCV(edges2)
#drawContoursCV(image2, contours2, hierarchy2)