#include <bits/stdc++.h>
using namespace std;
using ul = size_t;
using ll = long long;

void solve() {
    int size;
    string s;
    cin >> size >> s;
    ll ans  =0;
    for(int i = 0; i < s.size(); ++i) {
        if(s[i]!='0') {
            ans += s[i] - '0' + 1;
        }
    }
    if(s[s.size()-1]!='0'){
        ans--;
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