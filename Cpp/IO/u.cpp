#include <iostream>
using namespace std;

int main() {
  int m, n, r1, r2, r;

  cin >> n;
  cin >> m;

  r1 = m % n;
  r2 = n % m;
  r = r2 * r1 + 1;

  cout << r;
  return 0;
}
