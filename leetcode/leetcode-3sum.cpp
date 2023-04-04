#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

static constexpr int OOR = 99999999;
vector<int> test = {
    -13, 11,  11,  0,   -5,  -14, 12,  -11, -11, -14, -3,  0,   -3,  12, -1,
    -9,  -5,  -13, 9,   -7,  -2,  9,   -1,  4,   -6,  -13, -7,  10,  10, 9,
    7,   13,  5,   4,   -2,  7,   5,   -13, 11,  10,  -12, -14, -5,  -8, 13,
    2,   -2,  -14, 4,   -8,  -6,  -13, 9,   8,   6,   10,  2,   6,   5,  -10,
    0,   -11, -12, 12,  8,   -7,  -4,  -9,  -13, -7,  8,   12,  -14, 10, -10,
    14,  -3,  3,   -15, -14, 3,   -14, 10,  -11, 1,   1,   14,  -11, 14, 4,
    -6,  -1,  0,   -11, -12, -14, -11, 0,   14,  -9,  0,   7,   -12, 1,  -6};

int getmin(const vector <int> &v) {
  for(int i = 0; i < v.size(); ++i) {
    if(i != OOR)
      return v[i];
  }
}

int getmax(const vector <int> &v) {
  for(int i = v.size() - 1; i > -1; --i) {
    if(i != OOR)
      return v[i];
  }
}
vector<vector<int>> threeSum(vector<int>& nums) {
  sort(nums.begin(), nums.end());
  vector<unordered_map<int, set<vector<int>>>> table;
  // [how many numbers - 1][sum of the numbers][state i.e. whats left][index of
  // state]

  if (nums.size() < 3)
    return {};

  // level 0, -1 element
  table.emplace_back();
  for (int i = 0; i < nums.size(); ++i) {
    const auto tmp = nums[i];
    nums[i] = OOR;
    table[0][tmp].insert(nums);
    nums[i] = tmp;
  }

  table.emplace_back();
  for (auto& [sum, states] : table[0]) {
    for (auto state : states) {
      for (auto& val : state) {
        if (val != OOR) {
          const int tmp = val;
          val = OOR;
          const auto min = getmin(state);
          const auto max = getmax(state);
          if((sum + tmp + max >= 0) && (sum + tmp + min <= 0))
            table[1][sum + tmp].insert(state);
          val = tmp;
        }
      }
    }
  }

  table.emplace_back();
  for (auto& [sum, states] : table[1]) {
    for (auto state : states) {
      for (auto& val : state) {
        if (val != OOR) {
          const int tmp = val;
          val = OOR;
          if(sum + tmp == 0)
            table[2][sum + tmp].insert(state);
          val = tmp;
        }
      }
    }
  }

  const auto& states_sum0_elem3 = table[2][0];
  set<vector<int>> sol;
  for (const auto& state : states_sum0_elem3) {
    vector<int> tmp;
    for (int i = 0; i < state.size(); ++i) {
      if (state[i] == OOR)
        tmp.push_back(nums[i]);
    }
    sol.insert(tmp);
  }
  return vector<vector<int>>{sol.begin(), sol.end()};
}

int main() {
  threeSum(test);
  return 0;
}
