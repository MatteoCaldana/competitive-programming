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

static constexpr int T[4] = {1, 2, 3, 5};
static constexpr int MAX = 169000000;

vector<int> merge(vector<int>& l, int n) {
  l.push_back(MAX);
  l[n] = MAX;
  vector<int> res;
  int i[4] = {0};
  while (i[0] + i[1] + i[2] + i[3] != 4 * n) {
    int imin = -1, vmin = MAX - 1;
    for (int j = 0; j < 4; ++j) {
      const int v = l[i[j]] * T[j];
      if (vmin > v) {
        vmin = v;
        imin = j;
      }
    }
    if (res.size() == 0 || res.back() != vmin)
      res.push_back(vmin);
    i[imin]++;
  }
  return res;
}

int nthUglyNumber(int n) {
  vector<int> v = {1};
  for (int i = 0; i < n; ++i) {
    v = merge(v, i + 1);
    cout << "-----------------------" << endl;
    cout << v << endl;
    cout << "///////////////////////" << endl;
  }
  return v[n];
}

int main() {
  cout << nthUglyNumber(1690) << endl;
  return 0;
}