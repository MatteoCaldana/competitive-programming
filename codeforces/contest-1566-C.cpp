#include <bits/stdc++.h>
using namespace std;
using ui = size_t;

#define fi first
#define se second
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define rsz resize
#define len(x) (int) (x).size()

#define ff(i,a,b) for (int i = (a); i < (b); ++i)
#define ff0(i,a) ff(i,0,a)
#define rr(i,a,b) for (int i = (b)-1; i >= (a); --i)
#define rr0(i,a) rr(i,0,a)
#define fe(a,x) for (auto& a: x)
 
template <class T> void imi(T& a, T b) { if(b < a) a = b; }
template <class T> void ima(T& a, T b) { if(b > a) a = b; }

void solve() {
    int size;
    string s1, s2;
    cin >> size;
    cin >> s1;
    cin >> s2;
    int ans = 0;
    for(int i = 0; i < size; ++i) {
        if((s1[i] == '0' && s2[i] == '1')|| (s2[i] == '0' && s1[i] == '1')) {
            ans += 2;
        } else if ((i < size - 1) &&(s1[i+1] == s2[i+1]) && (s1[i+1] != s1[i]))  {
            i += 1;
            ans += 2;
        } else if (s1[i] == '0') {
            ans += 1;
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