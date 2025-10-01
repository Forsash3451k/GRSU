#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
    long long h, m, s, p, q, r, t_now, delta, result;
	cout << "Введите текущее время и на сколько часов нужно вернуться назад в формате h m s p q r: ";
	cin >> h >> m >> s >> p >> q >> r;

    t_now = h * 3600 + m * 60 + s;
    delta = p * 3600 + q * 60 + r;

    result = (t_now - delta) % (24 * 3600);
    if (result < 0) 
        result += 24 * 3600;

    cout << result / 3600 << " " << (result % 3600) / 60 << " " << result % 60 << endl;
    return 0;
}