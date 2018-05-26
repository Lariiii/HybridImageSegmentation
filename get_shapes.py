import matplotlib.pyplot as plt
import cv2

def edgeDetection(image):
    edges = cv2.Canny(image,100,200)
    plt.imshow(edges)
    plt.xticks([]), plt.yticks([])
    plt.savefig('results/edge')
    return edges

def findContoursCV(edges):
#    ret, thresh = cv2.threshold(edges,127,255, 0)
#    thresh = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    thresh = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return image, contours, hierarchy

def drawContoursCV(image, contours, hierarchy):
    for c in contours:
        cv2.drawContours(image, [c], -1, (0,255,0), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        break

def run():
    im = cv2.imread('results/dem.png')
    edges = edgeDetection(im)
    image, contours, hierarchy = findContoursCV(edges)
    drawContoursCV(image, contours, hierarchy)

