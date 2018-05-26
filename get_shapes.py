import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from datafiles import names

#plt.xticks([]), plt.yticks([])
#plt.savefig(outputName, dpi=500)

def edgeDetection(image, outputName='results/edge'):
    # Find Edges
    image = cv.Canny(image,100,600)
    plt.imshow(image)
    plt.show()

    # Blur Image
    kernel = np.ones((5, 5), np.float32) / 25
    image = cv.filter2D(image, -1, kernel)
    plt.imshow(image)
    plt.show()

    # Threshold Image
    #image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #ret, thresh1 = cv.threshold(dst, 127, 255, cv.THRESH_BINARY)
    #plt.imshow(image)
    #plt.show()

    return image

def findContoursCV(edges, adaptive=True):
    image, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return image, contours, hierarchy

def drawContoursCV(image, contours, hierarchy):
    cv.drawContours(
        image=image,
        contours=contours,
        contourIdx=-1,
        color=(0,255,0),
        thickness=0)
    cv.imshow("Image", image)
    cv.waitKey(0)

def getShowContours(imageFile):
    im = cv.imread(imageFile)
    edges = edgeDetection(im, outputName=imageFile+'_edge.png')
    image, contours, hierarchy = findContoursCV(edges)
    drawContoursCV(image, contours, hierarchy)
    return image, contours, hierarchy

def getShowContoursAll():
    for sourceName in names:
        file='results/'+sourceName+'.png'
        try:
            getShowContours(imageFile=file)
        except TypeError:
            print(file, 'not found')

def run():
    getShowContours('results/ndvi.png')