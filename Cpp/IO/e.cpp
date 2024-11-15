#include <iostream>
using namespace std;

int main() {
  int v, t, s;

  cin >> v;
  cin >> t;

  s = ((v * t) % 109 + 109) % 109;

  cout << s << endl;
  return 0;
}
