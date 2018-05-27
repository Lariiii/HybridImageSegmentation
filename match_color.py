import cv2
import numpy

from get_shapes import edgeDetection, findContoursCV, drawContoursCV

subjective_1 = cv2.imread('results/subjective1.png')
subjective_2 = cv2.imread('results/subjective2.png')

data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)



#edges2 = edgeDetection(im2)
#image2, contours2, hierarchy2 = findContoursCV(edges2)
#drawContoursCV(image2, contours2, hierarchy2)