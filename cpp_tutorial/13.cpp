#include <iostream>
#include <cmath>
using namespace std;

struct polar
{
  double distance;
  double angle;
};

struct rect
{
  double x;
  double y;
};

void rect_to_polar(const rect *pxy, polar *pda);
void show_polar(const polar *pda);

int main()
{
  rect rplace;
  polar pplace;
  cout << "Enter x and y values: ";
   
  while(cin >> rplace.x >> rplace.y)
  {
    rect_to_polar(&rplace, &pplace);
    show_polar(&pplace);
    cout << "Next two numbers(q to quit): ";
  }


  return 0;
}

void rect_to_polar(const rect *pxy, polar *pda)
{
  pda->distance = sqrt(pxy->x * pxy->x + pxy-> y * pxy->y);
  pda->angle = atan2(pxy->y, pxy->x);
}

void show_polar(const polar *pda)
{
  const double Rad_to_deg = 57.29577951;
  cout << "Distance = " << pda->distance <<endl;
  cout << "Angle =" << pda->angle*Rad_to_deg << " degree"<< endl;
}
