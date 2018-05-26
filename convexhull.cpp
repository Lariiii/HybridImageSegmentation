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
void cinN(unsigned int &x)
{
    register unsigned int c;

    x = 0;
    while((c = getchar_unlocked()) == ' ' || (c == '\n'));
    for (; (c>47 && c<58); c=getchar_unlocked())
        x = (x<<1) + (x<<3) + c - 48;
}
struct point {
	double x, y;
  int color;
  double ndvi;

	bool operator <(const point &p) const {
		return x < p.x || (x == p.x && y < p.y);
	}
};
double dist(point p1, point p2)
{
  return sqrt(( p2.x-p1.x)* ( p2.x-p1.x)+ (p2.y-p1.y)*(p2.y-p1.y));
}
double det(point p1, point p2, point p3)
{
  return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x);
}
double sum(point points[], int counter, point points2[] , int counter2)
{
  double sum = 0;
  for(int i = 0; i<counter-1; i++)
  {
    sum += dist(points[i], points[i+1]);
  }
  for(int i = 0; i<counter2-1; i++)
  {
    sum += dist(points2[i], points2[i+1]);
  }
  return sum;
}
double rnd(double d)
{
  return std::floor(d * 100 + 0.5)/100;
}
int main(void) {
  ios::sync_with_stdio(false);

  unsigned int tries, nails;
	point* upperHull = new point[2000001];
	point* lowerHull = new point[2000001];
  point* points = new point[2000001];


  string inX, inY, inCol;
  char* outX, outY, outCol;
	unsigned int x, y, color;
  double test1, test2 ,ndviVal;
	int lowerCounter = 0;
	int upperCounter= 0;

  //unordered_map<pair<int, int>,double> ndvi;
  double* test = new double[3000000];
  for(unsigned int j = 0; j< 45745; j++)
  {
    point newPoint;
    cin >> test1 >> test2 >> ndviVal;
    //cout <<  test1 << test2 << ndviVal << endl;
    ndviVal = rnd(ndviVal);
    test[j] = ndviVal;
    //cout << ndviVal << endl;
    //cout << x << y << color << endl;
    //cout << color << endl;
    //ndvi[make_pair(x,y)] = ndviVal;
  }
  //cout << "test" << endl;
  for(int l = 0; l<5; l++)
  {
    vector<point>* colorShaper = new vector<point>[42];
    int* counts = new int[42]();
    int* mi = new int[42]();
    int* minIndex = new int[42]();
    int* pushed = new int[9149]();
    for(unsigned int j = 0; j< 9149; j++)
    {

      point newPoint;
      cin >> x >> y >> color;
      //cout << x << y << color << endl;
      //cout << color << endl;
      newPoint.x =  x;
      newPoint.y =  y;
      newPoint.color = color;
      newPoint.ndvi = test[j+l*9149];
      cout << x << " " << y << " " << color << " " << endl;
      points[j+l*9149] = newPoint;

      //cout << newPoint.ndvi << endl;
      colorShaper[color].push_back(newPoint);
      counts[color]++;
      if(newPoint.y>=mi[color])
      {
        minIndex[color] = counts[color]-1;
      }
      assert(minIndex[color] <= counts[color]);
    }


    for(int k = 0; k<42; k++){
      if(counts[k] == 0)
        continue;
      point* upperHull = new point[2000001];
    	point* lowerHull = new point[2000001];
      int lowerCounter = 0;
      int upperCounter= 0;
      //cout << k << endl;
      //cout << counts[k] << endl;
      //cout << minIndex[k] << endl;
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
      double avg = 0;
    for(int i = 0; i<lowerCounter; i++)
    {
      //cout << lowerHull[i].x << " " << lowerHull[i].y << " " << k << endl;
      avg += lowerHull[i].ndvi;
    }
    for(int i = 0; i<upperCounter; i++)
    {
      //cout << upperHull[i].x << " " << upperHull[i].y << " " << k << endl;
      avg+= upperHull[i].ndvi;
    }


    avg = avg/(lowerCounter+upperCounter);
    //cout << avg << endl;
    for(unsigned int j = 0; j< 9149; j++)
    {

      point p = points[j+l*9149];
      for(int i = 0; i<lowerCounter; i++)
      {
        //cout << lowerHull[i].x << " " << lowerHull[i].y << " " << k << endl;
        if(abs(lowerHull[i].x-p.x)+abs(lowerHull[i].y-p.y)<=400)
        {
          if(abs(avg-points[j].ndvi)<0.1)
          {
            if(!pushed[j])
              cout << p.x << " " << p.y << " " << lowerHull[i].color << endl;
            pushed[j] = true;
          }
        }
      }
      for(int i = 0; i<upperCounter; i++)
      {
        //cout << upperHull[i].x << " " << upperHull[i].y << " " << k << endl;
        if(abs(upperHull[i].x-p.x)+abs(upperHull[i].y-p.y)<=400)
        {
          if(abs(avg-points[j].ndvi)<0.1)
          {
            if(!pushed[j])
            cout << p.x << " " << p.y << " " << upperHull[i].color << endl;
            pushed[j] = true;
          }
        }
      }


    }


    }
    }

  }
