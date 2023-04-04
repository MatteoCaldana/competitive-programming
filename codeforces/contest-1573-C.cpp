#include <bits/stdc++.h>
using namespace std;
using ul = size_t;
using ll = long long;

bool is_understood(const vector<int> &need, const vector<bool> &understood) {
    for(const auto ch : need) {
        if(!understood[ch-1])
            return false;
    }
    return true;
}

bool is_all_u(const vector<bool> & u) {
    for(const auto & b : u) {
        if(!b) return false;
    }
    return true;
}

void solve() {
    int size;
    cin >> size;
    vector<vector<int>> k(size);
    for(int i = 0; i < size; i++) {
        int n_need;
        cin >> n_need;
        k[i].resize(n_need);
        for(int j = 0; j < n_need; ++j) {
            cin >> k[i][j];
        }
    }
    vector<bool> understood(size, false);
    for(int i = 0; i < size + 1; i++) {
        const auto old = understood;
        for(int j = 0; j < size; j++) {
            //cout << "==" << k[j].size() << " " << is_understood(k[j], understood) << "\n";
            understood[j] = is_understood(k[j], understood);
        }
        if(is_all_u(understood)) {
            cout << i+1 << "\n";
            return;
        }
        if(old == understood) {
            cout << "-1\n";
            return;
        }
    }
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // -------------------------------------------------------------------------
    int size;
    cin >> size;
    while(size--)
        solve();

    // -------------------------------------------------------------------------
    return 0;
}