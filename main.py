from dataframeToImage import dataframeToImage
from dataPreprocessing import *
import approach_shapeMatching
import approach_colorMatching
import approach_boostMatching

def main():
    # Choose the approach you want to execute
    generatePNGs = False
    shapeMatching = True
    colorMatching = False
    subjectiveMatching = False
    boostMatching = False

    # Generate the necessary png pictures for computer vision (cv) processing
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
        # Choose whatever data you want to correlate using computer vision
        # Choose from the PNG's above
        _ = approach_shapeMatching.run('results/corine.png', subjectiveIntegration=False, show=True, outputPath="test.png")

    if subjectiveMatching:
        # Choose a subjective picture e.g. subjective1.png or subjective2.png
        # Most reasonable results for subjective1.png
        _ = approach_shapeMatching.run('results/subjective1.png', subjectiveIntegration=True, show=True)

    if colorMatching:
        # No possible data options
        _ = approach_colorMatching.run(show=True)

    if boostMatching:
        # Choose any data you want from the pngs
        _ = approach_boostMatching.run("results/corine.png")


if __name__ == "__main__":
    main()