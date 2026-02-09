#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    ll n;
    cin >> n;

    ll ris = n/5;
    if(n%5 != 0) ris++;

    cout << ris;
    return 0;
}