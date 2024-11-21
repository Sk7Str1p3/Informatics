#include <iostream>
using namespace std;

int main() {
  int a, a1, a2, a3, a4, r;

  cin >> a;

  a1 = a / 1000;
  a2 = a / 100 % 10;
  a3 = a / 10 % 10;
  a4 = a % 10;
  r = (a1 - a4) - (a2 - a3) + 1;

  cout << r << endl;
  return 0;
}
