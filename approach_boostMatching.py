import cv2
import numpy

import approach_shapeMatching
import approach_colorMatching

def run():
    heatMapShapes = approach_shapeMatching.run('results/corine.png', subjectiveIntegration=False, show=False)
    colorMapImage = approach_colorMatching.run(show=False)

    for shape in heatMapShapes:
        colorMapImage = cv2.fillPoly(numpy.asarray(colorMapImage), pts=[shape[0]], color=200)
        colorMapImage = cv2.fillPoly(numpy.asarray(colorMapImage), pts=[shape[1]], color=150)

    cv2.imshow("ColorMap", numpy.asarray(colorMapImage))
    cv2.waitKey(0)

run()