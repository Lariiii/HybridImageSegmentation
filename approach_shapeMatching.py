import matplotlib.pyplot as plt
import cv2
import numpy
import math
from PIL import Image
import copy
from getContours import edgeDetection, findContoursCV, drawContoursCV

def drawShape(shapes, edges):
    # Draw a shape to the image
    image = Image.fromarray(edges)
    image = cv2.fillPoly(numpy.asarray(image), pts=[shapes], color=(255, 255, 0))
    return image

def drawHeatmap(heatmap, shapes_1, shapes_2):
    # Draw both shapes on the heat map
    heatmap1 = cv2.fillPoly(numpy.asarray(heatmap), pts=[shapes_1], color=100)
    heatmap2 = cv2.fillPoly(numpy.asarray(heatmap), pts=[shapes_2], color=50)
    heatmap = heatmap1 + heatmap2
    return heatmap

def euclideanDistance(contour1, contour2):
    # Calculate the distance between 2 shape center points
    org_M = cv2.moments(contour1)
    org_cX = int(org_M["m10"] / org_M["m00"])
    org_cY = int(org_M["m01"] / org_M["m00"])

    dest_M = cv2.moments(contour2)
    dest_cX = int(dest_M["m10"] / dest_M["m00"])
    dest_cY = int(dest_M["m01"] / dest_M["m00"])

    dist = math.sqrt((dest_cX - org_cX) ** 2 + (dest_cY - org_cY) ** 2)
    return dist

def filterContours(contours):
    # Discard very small contours, e.g. noise
    contoursSmall = []
    for shape in contours:
        if len(shape) > 5:
            contoursSmall.append(shape)
    print("Contours Length: "+str(len(contoursSmall)))
    return contoursSmall

def run(filePath, subjectiveIntegration, show, outputPath=None):
    #ToDo: Refactor

    # At first, we will read the image and get the edges
    # This is the technical image which you are trying to correlate with the merged subjective images
    im2 = cv2.imread(filePath)
    edges2 = edgeDetection(im2)

    # Here the image will be displayed for better debugging of thw Computer Vision Methods
    image2, contours2, hierarchy2 = findContoursCV(edges2)
    if show:
        drawContoursCV(image2, contours2)

    # Here we will decide wether we want to compare subjective 1 & 2 or a combination of subjective 1 and 2 with a
    # chosen image. The usual case you be the later -> the combination of 1 & 2 in contrast to a chosen image

    if subjectiveIntegration:
        img_part1 = cv2.imread('results/subjective2.png')
        img_part2 = cv2.imread('results/subjective2.png')
    else:
        img_part1 = cv2.imread('results/subjective1.png')
        img_part2 = cv2.imread('results/subjective2.png')

    # Calculate the Edges of the 2 subjectives
    edges_part1 = edgeDetection(img_part1)
    edges_part2 = edgeDetection(img_part2)

    # Layer the 2 images over each other with equal weights
    edges1 = cv2.addWeighted(edges_part1,0.5,edges_part2,0.5,0)

    # Show the intermediate Images if you want to
    image1, contours1, hierarchy1 = findContoursCV(edges1)
    if show:
        drawContoursCV(image1, contours1)
        cv2.imshow("abc1", edges1)
        cv2.imshow("abc2", edges2)

    # Filter out the noise in the contours
    # Meaning that smaller shapes consisting of only a few points get discarded
    contoursSmallOrg = filterContours(contours1)
    contoursSmallDest = filterContours(contours2)

    # Create a copy of the basic shape as background for the "heat map"
    # The Heatmap is more of a correlation between the shapes found in subjective 1 & 2 vs the chosen image
    # Was at the time of coding meant do work abit differently
    edgeHeatmap = copy.deepcopy(edges1)

    # Extract the Heatmap Shapes to be used in other approaches
    heatmapShapes = []

    # Compare every discovered contour in the subjective merge image with every contour in the chosen image
    for i, org_contour in enumerate(contoursSmallOrg):
        for dest_contour in contoursSmallDest:
            # Proceed if a contour combination is not larger or smaller than 10% of the original contour
            # Furthermore, the distance between the centers of the shaped needs to be within 30 pixels
            if len(org_contour) * 1.1 > len(dest_contour) and len(org_contour) * 0.9 < len(dest_contour) and euclideanDistance(org_contour, dest_contour) < 30:

                # Calculate a score of how similar the 2 contours are
                # Invariant to size and rotation, only the shape is considered
                # If the 2 contours are similar enough, proceed
                ret = cv2.matchShapes(org_contour, dest_contour, 1, 0.0)
                if ret < 1.25:
                    # Draw the 2 contours on the heat map and append the shape to the shape collection
                    # ToDo: Draw a line between the 2 contours to see the connection
                    drawHeatmap(edgeHeatmap, dest_contour, org_contour)
                    heatmapShapes.append((org_contour, dest_contour))
                    if show:
                        # Plot a pair of contours to validate similarity as human
                        plt.subplot(121), plt.imshow(drawShape(org_contour, edges1), cmap='gray')
                        plt.title('Original Shape'), plt.xticks([]), plt.yticks([])
                        plt.subplot(122), plt.imshow(drawShape(dest_contour, edges2), cmap='gray')
                        plt.title('Matched Shape'), plt.xticks([]), plt.yticks([])
                        #plt.show()
                        plt.clf()

    # Show the resulting heat map
    if show:
        plt.imshow(edgeHeatmap)
        plt.show()

    if outputPath != None:
        plt.imsave(outputPath, edgeHeatmap)

    return heatmapShapes
