#include <iostream>
using namespace std;

int main() {
  int n, s, d, b1, b2, eh, e, em;
  cin >> n;

  s = 9 * 60;
  d = 45;
  b1 = 5;
  b2 = 15;

  e = s + n * d;
  e += (n - 1) * b1;
  e += (n - 1) / 2 * (b2 - b1);

  eh = e / 60;
  em = e % 60;
  cout << eh << " " << em;
  return 0;
}
