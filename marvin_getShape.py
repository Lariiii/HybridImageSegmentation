import matplotlib.pyplot as plt
import cv2

from get_shapes import edgeDetection, findContoursCV, drawContoursCV

im2 = cv2.imread('results/subjective2.png')
edges2 = edgeDetection(im2)
image2, contours2, hierarchy2 = findContoursCV(edges2)
drawContoursCV(image2, contours2, hierarchy2)