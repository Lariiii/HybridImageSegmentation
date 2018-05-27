import matplotlib.pyplot as plt
import cv2
import numpy
import math
from PIL import Image
import copy
from getContours import edgeDetection, findContoursCV, drawContoursCV

def drawShape(shapes, edges):
    image = Image.fromarray(edges)
    image = cv2.fillPoly(numpy.asarray(image), pts=[shapes], color=(255, 255, 0))
    return image

def drawHeatmap(heatmap, shapes_1, shapes_2):
    heatmap1 = cv2.fillPoly(numpy.asarray(heatmap), pts=[shapes_1], color=100)
    heatmap2 = cv2.fillPoly(numpy.asarray(heatmap), pts=[shapes_2], color=50)
    heatmap = heatmap1 + heatmap2
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

def filterContours(contours):
    contoursSmall = []
    for shape in contours:
        if len(shape) > 5:
            contoursSmall.append(shape)
    print("Contours Length: "+str(len(contoursSmall)))
    return contoursSmall

def run(filePath, subjectiveIntegration, show):
    #ToDo: Refactor
    im2 = cv2.imread(filePath)
    edges2 = edgeDetection(im2)
    image2, contours2, hierarchy2 = findContoursCV(edges2)
    if show:
        drawContoursCV(image2, contours2)

    if subjectiveIntegration:
        img_part1 = cv2.imread('results/subjective1.png')
        img_part2 = cv2.imread('results/subjective1.png')
    else:
        img_part1 = cv2.imread('results/subjective1.png')
        img_part2 = cv2.imread('results/subjective2.png')
    edges_part1 = edgeDetection(img_part1)
    edges_part2 = edgeDetection(img_part2)
    edges1 = cv2.addWeighted(edges_part1,0.5,edges_part2,0.5,0)
    image1, contours1, hierarchy1 = findContoursCV(edges1)
    if show:
        drawContoursCV(image1, contours1)

    if show:
        cv2.imshow("abc1", edges1)
        cv2.imshow("abc2", edges2)

    contoursSmallOrg = filterContours(contours1)
    contoursSmallDest = filterContours(contours2)

    edgeHeatmap = copy.deepcopy(edges1)
    heatmapShapes = []

    for i, org_contour in enumerate(contoursSmallOrg):
        for dest_contour in contoursSmallDest:
            if len(org_contour) * 1.1 > len(dest_contour) and len(org_contour) * 0.9 < len(dest_contour) and euclideanDistance(org_contour, dest_contour) < 30:
                ret = cv2.matchShapes(org_contour, dest_contour, 1, 0.0)
                if ret < 1.25:
                    drawHeatmap(edgeHeatmap, dest_contour, org_contour)
                    heatmapShapes.append((org_contour, dest_contour))
                    if show:
                        plt.subplot(121), plt.imshow(drawShape(org_contour, edges1), cmap='gray')
                        plt.title('Original Shape'), plt.xticks([]), plt.yticks([])
                        plt.subplot(122), plt.imshow(drawShape(dest_contour, edges2), cmap='gray')
                        plt.title('Matched Shape'), plt.xticks([]), plt.yticks([])
                        plt.show()
                        plt.clf()

    if show:
        plt.imshow(edgeHeatmap)
        plt.show()

    return heatmapShapes
