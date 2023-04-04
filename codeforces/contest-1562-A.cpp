#include <bits/stdc++.h>

int max_mod(const int &a, const int &b) {
    int B = b;
    if( B % 2 == 1 ) {
        B++;
    }
    if(a <= B / 2) {
        return (B / 2) - 1;
    } else {
        return b % a;
    }
}

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int size;
    vector<pair<int,int>> arr;
    cin >> size;
    arr.resize(size);
    for(int i = 0; i < size; ++i) {
        cin >> arr[i].first >> arr[i].second;
    }
// -----------------------------------------------------------------------------
    for(const auto &p : arr) {
        cout << max_mod(p.first, p.second) << "\n";
    }

    return 0;
}