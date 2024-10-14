#include <iostream>
using namespace std;

int main() {
  int N, K;
  cin >> N;
  cin >> K;
  cout << (K - (K % N)) / N << endl;
  return 0;
}
