#include <iostream>
using namespace std;

int main() {
  int n, m, d;

  cin >> n;
  cin >> m;

  d = (m + n - 1) / n;

  cout << d;
  return 0;
}
