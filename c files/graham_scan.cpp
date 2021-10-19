#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <math.h>
#include <stdbool.h>
#include <set>
#include <stack>
#include <algorithm>
using namespace std;

#define col 0
#define cw 1
#define ccw 2

typedef struct intPoint{
    int x;
    int y;
}intPoint;


//anchor point to polar sort the rem points
intPoint p;
//Global vector
vector <intPoint> resHull;

/*
orientation of 3 points depends on their slope.
if diff of slopes is positive,then there is RIGHT turn ie cw else if neg then
ccw ie LEFT or else collinear if 0
*/
int orientationOfPoints(intPoint p,intPoint q,intPoint r){
	//find diff between slope
	int resM = (q.y-p.y)*(r.x-q.x) - (q.x-p.x)*(r.y-q.y);
	cout << "Orientation:"<<resM<<endl;
	if(resM == 0) return col; //collinear
	if(resM>0) return cw;
	return ccw;
}

int euclidsDist(intPoint p1,intPoint p2){
	return (p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y);
}

void oriPrinter(int x){
	if(x==col) {cout<<"Collinear\n";return;}
	if(x==cw) {cout<<"Clockwise\n";return;}
	cout<<"Anti clockwise\n";
}

//sorting based on polar angles from the anchor point
int polAngSorter(const void* vp1,const void* vp2){
	intPoint p1 = *((intPoint*)vp1);
	intPoint p2 = *((intPoint*)vp2);
	int ori = orientationOfPoints(p,p1,p2);
	switch(ori){
		//if they are collinear then use euclids distance
		case col:
		if(euclidsDist(p,p2)>=euclidsDist(p,p1)) return -1;
		return 1;

		case cw:
		return 1;

		case ccw:
		return -1;

		default:
		printf("\nUnable to sort?\n");
		return 0;
		break;
	}
}

//get the element just below the top
intPoint justBelowTop(stack <intPoint>* stk){
	intPoint theTop = stk->top();
	stk->pop();
	intPoint retVal = stk->top();
	stk->push(theTop);
	return retVal;
}

void pointPrinter(intPoint pt){
    cout << '(' << "X:" << pt.x << ','<< "y:" <<pt.y << ')' << ',' << endl;
}

void convexHull(vector <intPoint> points){
	//finding the bottom most point out of all the points
	intPoint min_point = points.at(0);
	int min_index = 0;
	int i = 0;
	for(auto pt : points){
		//check which is more bottom
		if(pt.y<min_point.y){
			min_point = pt;
			min_index = i;
		}
		//if y coord is same the check for x coordinate
		else if(pt.y == min_point.y && pt.x < min_point.x){
			min_point = pt;
			min_index = i;
		}
		i++;
	}
	cout<<"Bottom most point : \n";
	pointPrinter(min_point);

	//swap the pos of bottom most point with the first index
	iter_swap(points.begin()+0,points.begin()+min_index);
	cout <<"After swapping : \n";
	for(int i = 0;i<points.size();i++){
		pointPrinter(points[i]);
	}

	/*
    sort the remaining n-1 points with respect to this anchor point
	ie the first point based on the POLAR angle in anti clock wise 
	dir because its a convex hull
    */
	p = points[0];

	qsort(&points[1],points.size()-1,sizeof(intPoint),polAngSorter);
	//cout << "Smallest polar angle point from ";pointPrinter(p);
	cout << "After sorting\n";
	for(int i = 0;i<points.size();i++){
		pointPrinter(points[i]);
	}

	/*
    now remove all the points with same polar angle from anchor point
	except for the farthest point
	the array is already sorted based on polar angles and also when 
	the polar angles where same we consdered their dist from p0 as the 
	factor for sorting.Hence the farthest point with similar polar
	angles is located at the end
    */
	for(int i = 1;i<points.size();i++){
		//iter through the sub vector to find same polar angle points
		int j = i;
		//count the indexes with same polar angles
		while(j< (points.size()-1) && 
			orientationOfPoints(p,points[j],points[j+1]) == col){
			j++;
		}
		//erase from i to j if i!=j
		if(i!=j){
			cout << "i "<<i<<endl;
			cout << "j "<<j<<endl;
			cout << j-i << " Dups found,removing them..\n";
			points.erase(points.begin()+i,points.begin()+(j));
		}
	}

	cout << "After removing duplicates : \n";
	for(int i = 0;i<points.size();i++){
		pointPrinter(points[i]);
	}

	//if the new vec has LT 3 points,then no convex hull formed
	if(points.size()<3) return ;

	//create the stack to store the points
	//push the first three points p0,p1,p2
	stack <intPoint> stk;
	cout << "Pushing.....\n";
	stk.push(points[0]);
	pointPrinter(points[0]);
	stk.push(points[1]);
	pointPrinter(points[1]);
	stk.push(points[2]);
	pointPrinter(points[2]);
	/*
	|p2|
	|p1|
	|p0|
	----
	*/

	//now start analysing the points from p3
	for(int i = 3;i<points.size();i++){
		cout << "Inside For loop \n";
		/*
        check the orientation ie angle formed from the point at the top 
		of the stack with the curr iter point,if its to thee right ie 
		cw(CONCAVE),then violates convex hull rule
        */

		pointPrinter(points[i]);
		while(stk.size()>1 && 
			orientationOfPoints(justBelowTop(&stk),stk.top(),points[i]) != ccw)
				stk.pop();
		//push the next point under consideration
		stk.push(points[i]);
	}
	cout<<"stk size:"<<stk.size()<<endl;
	cout<<"points arr size "<<points.size()<<endl;

	//stack has all the points of the HULL
	cout<<"Result : \n";
	while(!stk.empty()){
		intPoint temp = stk.top();
		pointPrinter(temp);
		resHull.push_back(temp);
		stk.pop();
	}
}


int main(){
	vector <intPoint> points = {{0, 3}, {1, 1}, {2, 2}, {4, 4},
                      {0, 0}, {1, 2}, {3, 1}, {3, 3}};
    convexHull(points);
}