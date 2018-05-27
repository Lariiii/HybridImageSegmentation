import matplotlib.pyplot as plt
import cv2
import numpy
import math
from PIL import Image
import cv2 as cv
from get_shapes import edgeDetection, findContoursCV, drawContoursCV

im1 = cv2.imread('results/subjective1.png')
edges1 = edgeDetection(im1)
image1, contours1, hierarchy1 = findContoursCV(edges1)
drawContoursCV(image1, contours1, hierarchy1)

im2 = cv2.imread('results/subjective2.png')
edges2 = edgeDetection(im2)
image2, contours2, hierarchy2 = findContoursCV(edges2)
drawContoursCV(image2, contours2, hierarchy2)

def drawShape(shapes, edges, name="a"):
    #data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)
    data = edges

    colors = [255, 0, 0]

    for shape in shapes:
        data[shape[0][1]][shape[0][0]] = colors[0]

    image = Image.fromarray(data)
    image = cv2.fillPoly(numpy.asarray(image), pts=[shapes], color=(255, 255, 0))
    return image
    #cv.imshow("Image", numpy.asarray(image))
    #cv.imwrite("output/shape"+str(name)+".png", numpy.asarray(image))
    #cv.waitKey(0)

def euclideanDistance(contour1, contour2):
    org_M = cv2.moments(contour1)
    org_cX = int(org_M["m10"] / org_M["m00"])
    org_cY = int(org_M["m01"] / org_M["m00"])

    dest_M = cv2.moments(contour2)
    dest_cX = int(dest_M["m10"] / dest_M["m00"])
    dest_cY = int(dest_M["m01"] / dest_M["m00"])

    dist = math.sqrt((dest_cX - org_cX) ** 2 + (dest_cY - org_cY) ** 2)
    return dist

contoursSmallOrg = []
for shape in contours1:
    if len(shape) > 8:
        contoursSmallOrg.append(shape)
print(len(contoursSmallOrg))

contoursSmallDest = []
for shape in contours2:
    if len(shape) > 8:
        contoursSmallDest.append(shape)
print(len(contoursSmallDest))

for i, org_contour in enumerate(contoursSmallOrg):
    #drawShape(org_contour, i)
    for dest_contour in contoursSmallDest:
        if len(org_contour) * 1.1 > len(dest_contour) and len(org_contour) * 0.9 < len(dest_contour) and euclideanDistance(org_contour, dest_contour) < 30:
            ret = cv2.matchShapes(org_contour, dest_contour, 1, 0.0)
            #print(ret)
            if ret < 1.25:
                plt.subplot(121), plt.imshow(drawShape(org_contour, edges1), cmap='gray')
                plt.title('Original Shape'), plt.xticks([]), plt.yticks([])
                plt.subplot(122), plt.imshow(drawShape(dest_contour, edges2), cmap='gray')
                plt.title('Matched Shape'), plt.xticks([]), plt.yticks([])
                plt.show()




