#include <bits/stdc++.h>
using namespace std;

template <typename T>
std::ostream& operator<<(std::ostream& out, const std::vector<T>& v) {
  out << "{";
  size_t last = v.size() - 1;
  for (size_t i = 0; i < v.size(); ++i) {
    out << v[i];
    if (i != last)
      out << ", ";
  }
  out << "}";
  return out;
}

int nthSuperUglyNumber(int n, const vector<int>& primes) {
  if (n <= 0)
    return 0;
  if (n == 1)
    return 1;
  vector<int> idxs(primes.size(), 0);
  vector<int> dp(1); dp.reserve(n);
  dp[0] = 1;
  while (dp.size() < n) {
    int imin = -1, vmin = INT_MAX / 1001;
    for (int j = 0; j < primes.size(); ++j) {
      const int v = primes[j] * dp[idxs[j]];
      if (vmin > v) {
        vmin = v;
        imin = j;
      }
    }
    if(dp.back() != vmin)
      dp.push_back(vmin);
    idxs[imin]++;
  }
  return dp[n - 1];
}

int main() {
  cout << nthSuperUglyNumber(12, {2,7,13,19}) << endl;

  return 0;
}