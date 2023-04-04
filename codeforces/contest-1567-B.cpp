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

int sumXOR(int a) {
    int res = 0 ^ 0;
    ff0(i, a) {
        res ^= i; 
    }
    return res;
}

int sumXOR2(int a) {
    if( a % 4 == 0) {
        return 0;
    } else if (a % 4 == 1) {
        return a - 1;
    } else if (a % 4 == 3) {
        return a;
    } else {
        return 1;
    }
}

void solve(int a, int b) {
    const int res = sumXOR2(a);
    if(res == b) {
        cout << a << '\n';
    } else if (a!=(res^b)) { // add res^b     
        cout << a + 1 << '\n';
    } else { // cannot add it as it changes mex, add res^b+2^big and 2^big
        cout << a + 2 << '\n';
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // -------------------------------------------------------------------------
    int size;
    cin >> size;
    ff0(i, size) {
        int a, b;
        cin >> a >> b;
        solve(a, b);
    }

    // -------------------------------------------------------------------------
    return 0;
}