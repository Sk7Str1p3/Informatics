#include <iostream>
using namespace std;

int main() {
  int n, h, m;
  cin >> n;
  h = n % (60 * 24) / 60;
  m = n - n / 60 * 60;
  cout << h << " " << m;
  return 0;
}
