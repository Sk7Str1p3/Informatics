#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
  int a, b, m;

  cin >> a;
  cin >> b;

  m = (a + b + abs(a - b)) / 2;

  cout << m;
  return 0;
}
