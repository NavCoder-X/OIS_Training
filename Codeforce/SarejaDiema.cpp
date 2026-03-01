#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n; cin >> n;
    vi cards(n);
    for (int i = 0; i < n; i++)
        cin >> cards[i];

    int l = 0, r = n-1;
    vi points(2);
    int i = 0;
    while (l<=r)
    {
        if(cards[l]>cards[r]){
            points[i%2] += cards[l++];
        }else points[i%2] += cards[r--];
        i++;
    }
    cout << points[0] << " " << points[1];

    return 0;
}