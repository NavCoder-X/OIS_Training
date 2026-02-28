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
 
    unsigned viaggi, bundle, costoBiglietto, costoBundle;
    cin >> viaggi >> bundle >> costoBiglietto >> costoBundle;
    unsigned costoSoloBiglietti = costoBiglietto * viaggi;
    unsigned costoSoloBundle = costoBundle * (viaggi / bundle);
    unsigned costoBundleBiglietti = costoSoloBundle + (costoBiglietto * (viaggi % bundle));
    if(costoSoloBundle != costoBundleBiglietti) costoSoloBundle += costoBundle;
    cout << min({costoSoloBiglietti,costoSoloBundle,costoBundleBiglietti}) << endl;
    return 0;
}