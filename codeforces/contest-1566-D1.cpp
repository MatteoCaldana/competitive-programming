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
    int n, m;
    vector<int> a, idx;
    cin >> n >> m;
    a.resize(n*m);
    ff0(i, n*m) {cin >> a[i];}
    sort(a.begin(), a.end());
    int ans = 0;
    for(int row = 0; row < n; ++row) {
        int prec = a[]
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // -------------------------------------------------------------------------
    int size;
    while(size--)
        solve();

    // -------------------------------------------------------------------------
    return 0;
}