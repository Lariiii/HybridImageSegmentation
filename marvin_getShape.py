import matplotlib.pyplot as plt
import cv2

from get_shapes import edgeDetection, findContoursCV, drawContoursCV

im1 = cv2.imread('results/subjective1.png')
edges1 = edgeDetection(im1)
image1, contours1, hierarchy1 = findContoursCV(edges1)
drawContoursCV(image1, contours1, hierarchy1)

im2 = cv2.imread('results/subjective2.png')
edges2 = edgeDetection(im2)
image2, contours2, hierarchy2 = findContoursCV(edges2)
drawContoursCV(image2, contours2, hierarchy2)


for org_contours in contours1:
    for dest_contour in contours2:
