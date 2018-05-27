#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <limits>
#include <fstream>
#include <iomanip>
#include <cassert>
#include<map>
#include <unordered_map>


using namespace std;
// Important constants for the program to work

// Number of points in the files
const int numPoints = 45745;

//Number of grids we want to partition into, input files, should be sorted corresponding to the grids
const int numGrids = 5;

//Number of different clusters in the human made file
const int numClusters = 42;

//Simple Point Definition
struct point {
	double x, y;
  int color;
  double val;

	bool operator <(const point &p) const {
		return x < p.x || (x == p.x && y < p.y);
	}
};
// Euclidean Distance between two points
double dist(point p1, point p2)
{
  return sqrt(( p2.x-p1.x)* ( p2.x-p1.x)+ (p2.y-p1.y)*(p2.y-p1.y));
}
// Is used to determine if three points make a counterclockwise turn
double det(point p1, point p2, point p3)
{
  return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x);
}
int main(int argc, char* argv[]) {
  ios::sync_with_stdio(false);

  unsigned int tries, nails;

  point* points = new point[numPoints];
  double dist;
  int eps;
  if(argc <= 1)
  {
  // If no input parameters are given, those are the standard values.

   // dist = Distance in continuous value for two points to be similar
   dist = 0.1;

   // eps = Episilon distance for the neighborhood of a points
   eps = 800;

  }
 else
 {
   dist= atof(argv[1]);
   eps = atoi(argv[2]);
 }
  string inX, inY, inCol;
  char* outX, outY, outCol;
	unsigned int x, y, color;
  double in1, in2 ,val;
	int lowerCounter = 0;
	int upperCounter= 0;

  double* contValues = new double[3000000];

  // Reading the continuous values
  for(unsigned int j = 0; j< numPoints; j++)
  {
    cin >> in1 >> in2 >> val;
    contValues[j] = val;
  }
  // Reading the clustered values and saving them
  for(int l = 0; l<numGrids; l++)
  {
    vector<point>* colorShaper = new vector<point>[numClusters];
    int* counts = new int[numClusters]();
    int* mi = new int[numClusters]();
    int* minIndex = new int[numClusters]();
    for(unsigned int j = 0; j< numPoints/numGrids; j++)
    {

      point newPoint;
      cin >> x >> y >> color;
      newPoint.x =  x;
      newPoint.y =  y;
      newPoint.color = color;
      newPoint.val = contValues[j+l*numPoints/numGrids];
      cout << x << " " << y << " " << color << " " << endl;
      points[j+l*numPoints/numGrids] = newPoint;
      colorShaper[color].push_back(newPoint);
      counts[color]++;
      if(newPoint.y>=mi[color])
      {
        minIndex[color] = counts[color]-1;
      }
      assert(minIndex[color] <= counts[color]);
    }

    //Monotone Chain algorithm to compute the convex hull for each cluster
    for(int k = 0; k<numClusters; k++){
      if(counts[k] == 0)
        continue;
      point* upperHull = new point[2*numPoints+1];
      point* lowerHull = new point[2*numPoints+1];
      int lowerCounter = 0;
      int upperCounter= 0;
      point swapFirst = colorShaper[k][0];
      colorShaper[k][0] = colorShaper[k][minIndex[k]];
      colorShaper[k][minIndex[k]] = swapFirst;
      sort(colorShaper[k].begin(), colorShaper[k].end());
    for(unsigned int j = 0; j<counts[k]; ++j)
    {
      while(lowerCounter >=2 && det(lowerHull[lowerCounter-2], lowerHull[lowerCounter-1], colorShaper[k][j])<=0)
       lowerCounter--;
      lowerHull[lowerCounter++] = colorShaper[k][j];

      while(upperCounter >=2 && det(upperHull[upperCounter-2], upperHull[upperCounter-1], colorShaper[k][counts[k]-j-1])<=0)
       upperCounter--;
      upperHull[upperCounter++] = colorShaper[k][counts[k]-j-1];

    }
    //Computing the average value for the points on the hull
    double avg = 0;
    for(int i = 0; i<lowerCounter; i++)
    {
      avg += lowerHull[i].val;
    }
    for(int i = 0; i<upperCounter; i++)
    {
      avg+= upperHull[i].val;
    }
    avg = avg/(lowerCounter+upperCounter);
    // Printing each point that is close to the hull in both measurements
    for(unsigned int j = 0; j< numPoints/numGrids; j++)
    {

      point p = points[j+l*numPoints/numGrids];
      for(int i = 0; i<lowerCounter; i++)
      {
        if(abs(lowerHull[i].x-p.x)+abs(lowerHull[i].y-p.y)<=eps)
        {
          if(abs(avg-points[j].val)<dist)
          {
              cout << p.x << " " << p.y << " " << lowerHull[i].color << endl;
          }
        }
      }
      for(int i = 0; i<upperCounter; i++)
      {
        if(abs(upperHull[i].x-p.x)+abs(upperHull[i].y-p.y)<=eps)
        {
          if(abs(avg-points[j].val)<dist)
          {
            cout << p.x << " " << p.y << " " << upperHull[i].color << endl;
          }
        }
      }


    }

    }
    }

  }
