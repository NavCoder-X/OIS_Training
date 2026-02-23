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

double solve(double x){
    double l = 0, r = x;
    double esp = 1e-9;
    while (r-l > esp)
    {
        double mid = l + (r-l)/2;
        double midSquare = mid*mid;
        if(midSquare >= x) r = mid;
        else l = mid;
    }
    
    return l;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    double x; cin >> x;
    cout << solve(x) << endl;
    return 0;
}