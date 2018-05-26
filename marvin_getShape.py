import matplotlib.pyplot as plt
import cv2
import numpy
from PIL import Image
import cv2 as cv
from get_shapes import edgeDetection, findContoursCV, drawContoursCV

im1 = cv2.imread('results/subjective1.png')
edges1 = edgeDetection(im1)
image1, contours1, hierarchy1 = findContoursCV(edges1)
drawContoursCV(image1, contours1, hierarchy1)

im2 = cv2.imread('results/subjective2.png')
edges2 = edgeDetection(im2)
image2, contours2, hierarchy2 = findContoursCV(edges2)
drawContoursCV(image2, contours2, hierarchy2)

def drawShape(shapes):
    data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)

    colors = [255, 0, 0]

    for shape in shapes:
        data[shape[0][1]][shape[0][0]] = colors[0]

    image = Image.fromarray(data)
    cv.imshow("Image", numpy.asarray(image))
    cv.waitKey(0)



for org_contour in contours1:
    drawShape(org_contour)
    for dest_contour in contours2:
        ret = cv2.matchShapes(org_contour, dest_contour, 1, 0.0)
        if ret < 0.01:
            pass
            #print(ret)
            #print(org_contour)
            #print(dest_contour)

