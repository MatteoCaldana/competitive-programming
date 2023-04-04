#include <bits/stdc++.h>

using namespace std;

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

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

std::ostream& operator<<(std::ostream& out, ListNode* n) {
  out << "{";
  while (n) {
    out << n->val << ",";
    n = n->next;
  }
  out << "}";
  return out;
}

ListNode* vectorToList(const vector<int>& v) {
  if (v.size() == 0)
    return nullptr;
  ListNode* head = new ListNode(v[0]);
  ListNode* curr = head;
  for (size_t i = 1; i < v.size(); ++i) {
    curr->next = new ListNode(v[i]);
    curr = curr->next;
  }
  return head;
}

vector<ListNode*> makeTest(const vector<vector<int>>& t) {
  vector<ListNode*> res;
  for (const auto& v : t)
    res.push_back(vectorToList(v));
  return res;
}

int mymin(const vector<int>& v) {
  int mmin = INT_MAX - 1, idx = -1;
  for (int i = 0; i < v.size(); ++i) {
    if (v[i] < mmin) {
      mmin = v[i];
      idx = i;
    }
  }
  return idx;
}

ListNode* mergeKLists(vector<ListNode*>& lists) {
  cout << "base case" << endl;
  // base cases
  if (lists.size() == 0)
    return nullptr;
  if (lists.size() == 1)
    return lists[0];
  cout << "init vars" << endl;
  // init variables
  int num_alive = 0;
  vector<int> heads(lists.size());
  for (int i = 0; i < lists.size(); ++i) {
    num_alive += int(bool(lists[i]));
    heads[i] = lists[i] ? lists[i]->val : INT_MAX;
  }
  if (num_alive == 0)
    return nullptr;
  if (num_alive == 1) {
    const auto mmin = mymin(heads);
    return lists[mmin];
  }
  cout << "init head" << endl;
  // init head of solution
  ListNode* head;
  const auto mmin = mymin(heads);
  if (mmin == -1) {
    return nullptr;
  } else {
    head = lists[mmin];
    lists[mmin] = lists[mmin]->next;
    if (lists[mmin]) {
      heads[mmin] = lists[mmin]->val;
    } else {
      heads[mmin] = INT_MAX;
      num_alive--;
    }
  }
  cout << "loop" << endl;
  // loop
  ListNode* curr = head;
  while (num_alive) {
    cout << heads << endl;
    const auto mmin = mymin(heads);

    curr->next = lists[mmin];
    curr = curr->next;
    lists[mmin] = lists[mmin]->next;
    if (lists[mmin]) {
      heads[mmin] = lists[mmin]->val;
    } else {
      heads[mmin] = INT_MAX;
      num_alive--;
    }
  }
  return head;
}

int main() {
  auto TEST1 = makeTest({{1, 4, 5}, {1, 3, 4}, {2, 6}});
  for (auto l : TEST1)
    cout << l << endl;
  auto r = mergeKLists(TEST1);
  cout << r << endl;

  return 0;
}