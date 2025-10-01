#include <iostream>
#include <cmath>

using namespace std;

int main2()
{
	setlocale(LC_ALL, "Russian");
	long double x1, y1, x2, y2, x3, y3, r1, r2, r3, buf, k1, k2;
	bool isline = false;

	cout << "Введите координаты точек треугольника в формате x1, y1, x2, y2, x3, y3: ";
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

	r1 = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
	r2 = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2));
	r3 = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2));


	if (r1 > r2 && r1 > r3)
	{
		buf = r3;
		r3 = r1;
		r1 = buf;
		if (r1 > r2)
		{
			buf = r2;
			r2 = r1;
			r1 = buf;
		}
	}
	else if (r1 > r2)
	{
		buf = r2;
		r2 = r1;
		r1 = buf;
		if (r2 > r3)
		{
			buf = r3;
			r3 = r2;
			r2 = buf;
		}
	}
	else if (r1 > r3)
	{
		buf = r3;
		r3 = r2;
		r2 = buf;

		buf = r2;
		r2 = r1;
		r1 = buf;
	}

	if ((y2 - y1)/(x2 - x1) == (y3 - y2)/(x3 - x2))
		isline = true;

	if (r1 + r2 + r3 == 0)
	{
		cout << "Вы ввели координаты точки, а не треугольника";
		return 0;
	}
	if (r1 == 0 || r2 == 0 || r3 == 0 || isline)
	{
		cout << "Вы ввели координаты отрезка, а не треугольника";
		return 0;
	}

	cout << "Периметр равен: " << r1 + r2 + r3;
	return 0;
}