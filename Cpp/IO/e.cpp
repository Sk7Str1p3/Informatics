#include <iostream>
#include <ostream>
using namespace std;

int main() {
  int v, t;
  cin >> v;
  cin >> t;
  cout << ((v * t) % 109 + 109) % 109 << endl;
  return 0;
}
