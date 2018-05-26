import matplotlib.pyplot as plt
import cv2 as cv
from datafiles import names

def edgeDetection(image, show=True, outputName='results/edge'):
    edges = cv.Canny(image,100,200)
    if show:
        plt.imshow(edges)
        plt.xticks([]), plt.yticks([])

    if outputName is not None: plt.savefig(outputName)

    return edges

def findContoursCV(edges, adaptive=True):
    if adaptive:
        # https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html
        thresh = cv.adaptiveThreshold(
            src=edges,
            maxValue=255,
            adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,  #cv.ADAPTIVE_THRESH_MEAN_C
            thresholdType=cv.THRESH_BINARY_INV,
            blockSize=11,
            C=0)
    else:
        _, thresh = cv.threshold(edges, 127, 255, 0)

    image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return image, contours, hierarchy

def drawContoursCV(image, contours, hierarchy=None, name="Image"):
    cv.drawContours(
        image=image,
        contours=contours,
        contourIdx=0,
        color=(0,255,0),
        thickness=0)
    cv.imshow(name, image)
    cv.waitKey(0)

def getShowContours(imageFile='results/dem.png'):
    im = cv.imread(imageFile)
    edges = edgeDetection(im, outputName=imageFile+'_edge.png')
    image, contours, hierarchy = findContoursCV(edges)
    drawContoursCV(image, contours, hierarchy, name=imageFile)
    return image, contours, hierarchy

def getShowContoursAll():
    for sourceName in names:
        file='results/'+sourceName+'.png'
        try:
            getShowContours(imageFile=file)
        except TypeError:
            print(file, 'not found')

#getShowContoursAll()