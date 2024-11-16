#include <iostream>
using namespace std;

int main() {
  int h1, m1, s1, h2, m2, s2, d;

  cin >> h1;
  cin >> m1;
  cin >> s1;
  cin >> h2;
  cin >> m2;
  cin >> s2;

  d = (h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1);

  cout << d;
  return 0;
}
