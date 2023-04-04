#pragma GCC optimize("Ofast, unroll-loops", "omit-frame-pointer","inline")
#pragma GCC option("arch=native","tune=native","no-zero-upper")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native,avx2")

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

constexpr size_t MAX = 200'001ull;
int cumsum[MAX];
int zeroclump[MAX];
char s[MAX];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    // -------------------------------------------------------------------------

    scanf("%s",s);
	const int size = strlen(s);
    
    cumsum[0] = 0;
    ff(i, 0, size) {
        cumsum[i + 1] = cumsum[i] + (s[i] == '1');
    }

    int last = 0;
    bool inzeroclump = false;
    ff0(i, size) {
        if(inzeroclump) {
            if(s[i] == '1') {
                inzeroclump = false;
                ff(j, last, i + 1) {
                    zeroclump[j] = i;
                }
                last = i + 1;
            }
        } else if(s[i] == '0') {
            inzeroclump = true;
        } else {
            zeroclump[i] = i;
            last = i + 1;
        }
    }
    zeroclump[size-1] = size - 1;

    int ans = 0;
    int trimsize = size;
    while(s[trimsize-1] == '0')
        trimsize--;

    ff0(i, trimsize) {
        ff(j, zeroclump[i] + 1, size + 1) {
            const auto ones = cumsum[j] - cumsum[i];
            ans += (j-i) % ones == 0;
        }
    }
    cout << ans << '\n';

    // -------------------------------------------------------------------------
    return 0;
}