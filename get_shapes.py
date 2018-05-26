import matplotlib.pyplot as plt
import cv2

def edgeDetection(image):
    edges = cv2.Canny(im,100,200)
    plt.imshow(edges)
    plt.xticks([]), plt.yticks([])
    plt.savefig('results/edge')
    #plt.subplot(121), plt.imshow(im,cmap="gray")
    #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    #plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    #plt.show()
    return edges

def findContoursCV(edges):
    ret, thresh = cv2.threshold(edges,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return image, contours, hierarchy

def drawContoursCV(image, contours, hierarchy):
    for c in contours:
        cv2.drawContours(image, [c], -1, (0,255,0), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        break

im = cv2.imread('results/ndvi.png')
edges = edgeDetection(im)
image, contours, hierarchy = findContoursCV(edges)
drawContoursCV(image, contours, hierarchy)

