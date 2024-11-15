#include <iostream>
using namespace std;

int main() {
  int N, K, L;

  cin >> N;
  cin >> K;

  L = (K - (K % N)) / N;

  cout << L;
  return 0;
}
