import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from datafiles import names

def showImage(image):
    plt.imshow(image)
    plt.show()

def edgeDetection(image):
    # Find Edges
    image = cv.Canny(image,100,600)
    #showImage(image)

    # Blur Image
    kernel = np.ones((3, 3), np.float32) / 25
    image = cv.filter2D(image, -1, kernel)
    #showImage(image)

    # Threshold Image
    #image = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #ret, image = cv.threshold(dst, 127, 255, cv.THRESH_BINARY)
    #showImage(image)

    return image

def findContoursCV(edges, adaptive=True):
    # Helper Function to find Contours
    image, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return image, contours, hierarchy

def drawContoursCV(image, contours):
    # Helper Function to draw contours
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
    edges = edgeDetection(im)
    image, contours, hierarchy = findContoursCV(edges)
    drawContoursCV(image, contours)
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