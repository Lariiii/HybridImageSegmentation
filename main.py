from dataframeToImage import dataframeToImage
from read_files import *
from dataPreprocessing import *
from getContours import *
import approach_shapeMatching
import approach_colorMatching



def main():
    # Data Reading
    getShowContours("results/subjective1.png")
    generatePNGs = False
    shapeMatching = True
    colorMatching = False

    if generatePNGs:
        dataframeToImage(read_subjective1(), 'results/subjective1.png')
        dataframeToImage(read_subjective2(), 'results/subjective2.png')
        dataframeToImage(read_corine(), 'results/corine.png')

        dataframeToImage(pruning(read_aspect1()), True, 'results/aspect1.png')
        dataframeToImage(pruning(read_aspect2()), True, 'results/aspect2.png')

        dataframeToImage(pruning(read_dem()), True, 'results/dem.png')
        dataframeToImage(pruning(read_ndvi()), True, 'results/ndvi.png')
        dataframeToImage(pruning(read_slope()), True, 'results/slope.png')

    if shapeMatching:
        approach_shapeMatching.run()

    if colorMatching:
        approach_colorMatching.run()



if __name__ == "__main__":
    main()