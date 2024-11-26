#include <iostream>
#include <ostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  if ((a != 1 && b != 1) or (a == 1 and b == 1)) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }

  return 0;
}
