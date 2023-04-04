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
    string s;
    cin >> s;
    while(s.back() == '1')
        s.resize(s.size()-1);
    bool all_zero = true, all_ones = true;
    for(char &c : s) {
        if( c == '1')
            all_zero = false;
        if( c == '0')
            all_ones = false;
    }
    if(all_ones) {
        cout << "0\n";
        return;
    }
    if(all_zero) {
        cout << "1\n";
        return;
    }
    
    
    int first_diff = 1;
    while(s[first_diff] == s[0]) {first_diff++;}
    int second_diff = first_diff + 1;
    while(second_diff < s.size() && s[second_diff] == s[first_diff]) {second_diff++;}
    if(second_diff == s.size()) {
        cout << "1\n";
        return;
    }
    cout << "2\n";
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