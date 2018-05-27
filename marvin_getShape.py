import matplotlib.pyplot as plt
import cv2
import numpy
import math
from PIL import Image
import copy
import cv2 as cv
from get_shapes import edgeDetection, findContoursCV, drawContoursCV

im2 = cv2.imread('results/corine.png')
edges2 = edgeDetection(im2)
image2, contours2, hierarchy2 = findContoursCV(edges2)
drawContoursCV(image2, contours2, hierarchy2)

img_part1 = cv2.imread('results/subjective1.png')
img_part2 = cv2.imread('results/subjective1.png')
edges_part1 = edgeDetection(img_part1)
edges_part2 = edgeDetection(img_part2)
edges1 = cv2.addWeighted(edges_part1,0.5,edges_part2,0.5,0)
image1, contours1, hierarchy1 = findContoursCV(edges1)
drawContoursCV(image1, contours1, hierarchy1)



#edges1[edges1[:, :, 1:].all(axis=-1)] = 0
#edges2[edges2[:, :, 1:].all(axis=-1)] = 0

#dst = cv2.addWeighted(edges1, 1, edges2, 1, 0)
#cv2.imshow("abc", dst)


cv2.imshow("abc1", edges1)
cv2.imshow("abc2", edges2)

def drawShape(shapes, edges, name="a"):
    #data = numpy.zeros((431, 337, 3), dtype=numpy.uint8)
    data = edges

    colors = [255, 0, 0]

    #for shape in shapes:
    #    data[shape[0][1]][shape[0][0]] = colors[0]

    image = Image.fromarray(data)
    image = cv2.fillPoly(numpy.asarray(image), pts=[shapes], color=(255, 255, 0))
    return image
    #cv.imshow("Image", numpy.asarray(image))
    #cv.imwrite("output/shape"+str(name)+".png", numpy.asarray(image))
    #cv.waitKey(0)

def drawHeatmap(heatmap, shapes_1, shapes_2):
    heatmap1 = cv2.fillPoly(numpy.asarray(heatmap), pts=[shapes_1], color=256)
    heatmap2 = cv2.fillPoly(numpy.asarray(heatmap), pts=[shapes_2], color=128)
    heatmap = cv2.addWeighted(heatmap1, 0.5, heatmap2, 0.5, 0)
    return heatmap

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
    if len(shape) > 5:
        contoursSmallOrg.append(shape)
print(len(contoursSmallOrg))

contoursSmallDest = []
for shape in contours2:
    if len(shape) > 5:
        contoursSmallDest.append(shape)
print(len(contoursSmallDest))

edgeHeatmap = copy.deepcopy(edges1)

for i, org_contour in enumerate(contoursSmallOrg):
    #drawShape(org_contour, i)
    for dest_contour in contoursSmallDest:
        if len(org_contour) * 1.1 > len(dest_contour) and len(org_contour) * 0.9 < len(dest_contour) and euclideanDistance(org_contour, dest_contour) < 30:
            ret = cv2.matchShapes(org_contour, dest_contour, 1, 0.0)
            #print(ret)
            if ret < 1.25:
                drawHeatmap(edgeHeatmap, dest_contour, org_contour)
                plt.subplot(121), plt.imshow(drawShape(org_contour, edges1), cmap='gray')
                plt.title('Original Shape'), plt.xticks([]), plt.yticks([])
                plt.subplot(122), plt.imshow(drawShape(dest_contour, edges2), cmap='gray')
                plt.title('Matched Shape'), plt.xticks([]), plt.yticks([])
                #plt.show()
                plt.clf()

plt.imshow(edgeHeatmap)
plt.show()

