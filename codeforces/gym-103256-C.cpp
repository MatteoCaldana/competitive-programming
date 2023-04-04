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
    for(int i = 0; i < size; ++i) {
        if(arr[i] - 1 == i)
        res++;
    }

    cout << res;

    return 0;
}