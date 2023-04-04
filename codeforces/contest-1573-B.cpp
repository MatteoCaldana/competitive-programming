#include <bits/stdc++.h>
using namespace std;
using ul = size_t;
using ll = long long;

void solve() {
    int size;
    cin >> size;
    vector<int> a(size, 1'000'000), b(size, -1);
    for(int i = 0; i < size; i++) {
        cin >> a[i];
    }
    for(int i = 0; i < size; i++) {
        cin >> b[i];
    }
    for(int i = 1; i < size; i++) {
        a[i] = min(a[i-1], a[i]);
        b[i] = max(b[i-1], b[i]);
    }
    int ans = 2*1'000'000;
    for(int i = 0; i < size; ++i) {
        for(int j = 0; j < size; ++j) {
            if(a[i] < b[j]) {
                ans = min(ans, i+j);
                break;
            }
        }
    }
    
    cout << ans << "\n";
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