import cv2
import numpy

import approach_shapeMatching
import approach_colorMatching

def run(filename):
    # Get all the Heat Map Shapes
    heatMapShapes = approach_shapeMatching.run(filename, subjectiveIntegration=False, show=False)

    # Get the color-map
    colorMapImage = approach_colorMatching.run(show=False)

    # For each shape, draw it on the color-map to get a summarized view
    for shape in heatMapShapes:
        colorMapImage = cv2.fillPoly(numpy.asarray(colorMapImage), pts=[shape[0]], color=200)
        colorMapImage = cv2.fillPoly(numpy.asarray(colorMapImage), pts=[shape[1]], color=150)

    # Show the picture
    cv2.imshow("ColorMap", numpy.asarray(colorMapImage))
    cv2.waitKey(0)