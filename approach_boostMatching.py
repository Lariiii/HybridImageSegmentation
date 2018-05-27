import approach_shapeMatching
import approach_colorMatching

def run():
    heatMapShapes = approach_shapeMatching.run('resources/corine.png',subjectiveIntegration=False, show=False)
    colorMapImage = approach_colorMatching.createColorMap('resources/subjective1.png', 'resources/subjective2.png')