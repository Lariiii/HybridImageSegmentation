import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from datafiles import names

def edgeDetection(image, show=False, outputName='results/edge'):
    edges = cv.Canny(image,100,600)
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv.filter2D(edges, -1, kernel)
    thresh1 = cv.adaptiveThreshold(dst, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    #ret, thresh1 = cv.threshold(dst, 127, 255, cv.THRESH_BINARY)
    if show:
        plt.imshow(edges)
        plt.xticks([]), plt.yticks([])
        plt.show()

    plt.savefig(outputName, dpi=500)
    return thresh1

def findContoursCV(edges, adaptive=True):
    if adaptive:
        # https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html
        thresh = cv.adaptiveThreshold(
            src=edges,
            maxValue=255,
            adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,  #cv.ADAPTIVE_THRESH_MEAN_C
            thresholdType=cv.THRESH_BINARY_INV,
            blockSize=31,
            C=0)
    else:
        _, thresh = cv.threshold(edges, 127, 255, 0)

    image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
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