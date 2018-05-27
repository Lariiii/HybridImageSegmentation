from dataframeToImage import dataframeToImage
from read_files import *
from dataPreprocessing import *
from getContours import *
import approach_shapeMatching
import approach_colorMatching



def main():
    # Data Reading
    generatePNGs = True
    shapeMatching = False
    colorMatching = False
    subjectiveMatching = False

    if generatePNGs:
        dataframeToImage(read_subjective1(), 'results/subjective1.png')
        dataframeToImage(read_subjective2(), 'results/subjective2.png')
        dataframeToImage(read_corine(), 'results/corine.png')

        dataframeToImage(pruning(read_aspect1()), 'results/aspect1.png')
        dataframeToImage(pruning(read_aspect2()), 'results/aspect2.png')

        dataframeToImage(pruning(read_dem()), 'results/dem.png')
        dataframeToImage(pruning(read_ndvi()), 'results/ndvi.png')
        dataframeToImage(pruning(read_slope()), 'results/slope.png')

    if shapeMatching:
        _ = approach_shapeMatching.run('results/corine.png', subjectiveIntegration=False, show=True)

    if subjectiveMatching:
        _ = approach_shapeMatching.run('results/subjective2.png', subjectiveIntegration=True, show=True)

    if colorMatching:
        _ = approach_colorMatching.run(show=True)



if __name__ == "__main__":
    main()