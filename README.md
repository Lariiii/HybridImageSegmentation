# HybridImageSegmentation

This repository contains the concept and approaches to integrate human and technically sensed images into one segmented image.

## Approaches
### Shapematching
![Shapematching1](https://github.com/Lariiii/HybridImageSegmentation/blob/master/documentation_images/shapematching1.png)
![Shapematching2](https://github.com/Lariiii/HybridImageSegmentation/blob/master/documentation_images/shapematching2.png)
![Shapematching3](https://github.com/Lariiii/HybridImageSegmentation/blob/master/documentation_images/shapematching3.png)

### Colormatching
![Colormatching](https://github.com/Lariiii/HybridImageSegmentation/blob/master/documentation_images/colormatching.png)

### Boostmatching
![Boostmatching](https://github.com/Lariiii/HybridImageSegmentation/blob/master/documentation_images/Boostmatching.png)
The approach of Boostmatching combines several "Matching-Algorithms" to one Ensemble Framework. This is extensible to many more matching approaches.

### Convex Hull
![Convex Hull](https://github.com/Lariiii/HybridImageSegmentation/blob/master/documentation_images/hull.png)
Three steps are needed for calculating the possible points using a convex hull approach:

* Compiling the C Program:
    - g++ -std=c++1y convexhull.cpp#
* Executing the resulting binary:
    - You need the two text files, containing x and y coordinates and the corresponding labels/ values in those text files
    - Machine Made File: machine.txt
    - Human Made File: human.txt
    - Maximum difference for two points in the value of the first text file to be considered similar: max (default 0.1)
    - Maximum Manhattan Distance between two points in order to be in a neighborhood: dist (default 800)
    - Output file: out.text (In its current form, the output file will consist of an unordered list of points with a cluster for each point, a single point can be included multiple times with different clusters)
    -  cat machine.txt human.txt |./a.out max dist > output.txt
* Execute the generate_convex_png.py script

## Getting Started
* First, generate the png files by setting the generatePNGs() boolean to 'True' (afterwards change it back to 'False' to save computing time) 
* Choose the method you want in the main.py file by changing the corresponding boolean value to 'True'.
* The comments in the specific methods describe which parameters are required.


## Contributors
* [Larissa Hoffaeller](https://github.com/Lariiii)
* [Mirko Krause](https://github.com/Miroka96)
* [Jannik Peters](https://github.com/jannikpeters)
* [Marvin Thiele](https://github.com/MarvinThiele)
