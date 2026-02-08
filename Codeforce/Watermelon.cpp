#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

bool solve(int q){
    if(q <= 3) return 0;
    int i = 1, target = q/2+1;
    int p;

    for ( i = 0; i < target; i++)
    {
        p = q - i;
        if(p % 2 == 0 && i % 2 == 0) return 1;
    }
    
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int t;
    cin >> t;

    // bruteforce
    auto ris = solve(t);

    if(ris) cout << "YES";
    else cout << "NO";
    
    return 0;
}