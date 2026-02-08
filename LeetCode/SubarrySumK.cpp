#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, k, x, sum = 0;
    int ris = 0;
    map<int,int> PrefixSum;
    PrefixSum[0] = 1;
    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        cin >> x;
        sum += x;
        if(PrefixSum[sum - k] > 0){
            ris += PrefixSum[sum - k];
        }
        PrefixSum[sum]++;
    }

    cout << ris << endl;
    
    return 0;
}