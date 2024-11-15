#include <iostream>
using namespace std;

int main() {
  int a, b, n, s, sr, sk;

  cin >> a;
  cin >> b;
  cin >> n;

  s = a * n * 100 + b * n;
  sr = s / 100;
  sk = s % 100;

  cout << sr << " " << sk;
  return 0;
}
