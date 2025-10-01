#include <iostream>

using namespace std;

int main1()
{
	setlocale(LC_ALL, "Russian");
	double x, f; 

	cout << "Введите значение аргумента x : ";
	cin >> x;

	f=x*x*x+2.5*x*x-1.2;
	cout << "f(" << x << ") = " << f << endl;
	return 0;
}