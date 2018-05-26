import matplotlib.pyplot as plt
import cv2 as cv

def edgeDetection(image, show=True, outputname='results/edge'):
    edges = cv.Canny(image,100,200)
    if show:
        plt.imshow(edges)
        plt.xticks([]), plt.yticks([])

    if outputname is not None: plt.savefig(outputname)

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

def drawContoursCV(image, contours, hierarchy):
    #for c in contours:
    cv.drawContours(
        image=image,
        contours=contours,
        contourIdx=0,
        color=(0,255,0),
        thickness=0)
    cv.imshow("Image", image)
    cv.waitKey(0)
#    break

def run():
    im = cv.imread('results/dem.png')
    edges = edgeDetection(im)
    image, contours, hierarchy = findContoursCV(edges)
    drawContoursCV(image, contours, hierarchy)
