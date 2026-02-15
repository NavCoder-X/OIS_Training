#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

void balancedArray(int n){
    vi ris(n);
    ll sum = (n/4)*(2+n);
    ll oddSum = 0;
    int i = 0, j = n/2;
    ll x;
    for (x = 2; x < n; x+=2)
    {
        ris[i++] = x;
        ris[j++] = x-1;
        oddSum += x-1;
    }
    ris[i] = x;
    if(sum-oddSum & 1){
        cout << "YES" << endl;
        ris[j] = sum-oddSum;
        for (auto n: ris){
            cout << n << ' ';
        }
        cout << endl;
    }else cout << "NO" << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        balancedArray(n);
    }
    return 0;
}