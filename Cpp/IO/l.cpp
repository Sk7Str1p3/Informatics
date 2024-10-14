#include <iomanip>
#include <iostream>
using namespace std;

int main() {
  int n, h, m, s;
  cin >> n;
  h = n / (60 * 60) % 24;
  m = n % (60 * 60) / 60;
  s = n % 60;

  cout << h << ":" << setfill('0') << setw(2) << m << ":" << setfill('0')
       << setw(2) << s;

  return 0;
}
