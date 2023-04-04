#include <bits/stdc++.h>
using namespace std;
#define int         long long int
#define rep(i,a,b)  for (int i = a; i < b; ++i)
#define rrep(i,z,a) for (int i = z; i >= a; --i)
#define rep0(n)     for(int i = 0 ; i < n; ++i )
#define rep1(n)     for(int i = 1 ; i <= n; ++i )
#define tc          int test;cin>>test; while(test--)
#define all(v)      v.begin(),v.end()
#define pb          push_back
#define ff          first
#define ss          second
#define endl        "\n"
#define maxn        998244353
#define mod         1000000007
#define spc         " "
#define kill(x)     return cout<<x<<endl,0
#define ll          long long int
#define inf         5e18
const int N = 3005;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
int f(int x, int*a, int n)
{
	int ans = 0;
	int j = 0;
	for (int i = x; i < n; i += 2)
	{
		while (a[j] != 0)j++;
        
		ans += abs(i - j);
        cout << "==" << ans << '-'<< j << '\n';
		j++;
	}
	return ans;
}
int solve()
{
	int n;
	cin >> n;
	int a[n];
	int cnt[2] = {};
	rep0(n)cin >> a[i], a[i] %= 2, cnt[a[i]]++;
	if (n == 1)kill(0);
	if (abs(cnt[0] - cnt[1]) > 1)kill(-1);
	int ans = inf;
	if (n % 2)
	{
		if (cnt[0] > cnt[1])
			ans = f(0, a, n);
		else
			ans = f(1, a, n);
	}
	else
		ans = min(f(0, a, n), f(1, a, n));
 
	kill(ans);
}
signed main()
{
 
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int cases = 1;
	tc
	// cout << "Case #" << cases++ << ": ",
	solve();
	return 0;
}