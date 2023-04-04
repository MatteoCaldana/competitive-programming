#include <bits/stdc++.h>

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int size;
    vector<int> arr;
    cin >> size;
    arr.resize(size);
    for(int i = 0; i < size; ++i) {
        cin >> arr[i];
    }
    int res = 0;
    for(int i = 0; i < size/2; ++i) {
        res -= arr[2*i];
        res += arr[2*i+1];
    }

    cout << res;

    return 0;
}