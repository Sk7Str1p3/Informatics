#include <iostream>
using namespace std;

int main() {
  int a,r;

  cin >> a;

  r = a + 2 - a % 2;

  cout << r << endl;
  return 0;
}
