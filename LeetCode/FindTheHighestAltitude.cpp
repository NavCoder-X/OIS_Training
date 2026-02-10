#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int largestAltitude(vi & gain){
    vi prefix;
    int sum = 0, massimo = 0;

    // prefix sum
    prefix.push_back(0);
    for (int i = 0; i < gain.size(); i++)
    {
        sum+=gain[i];
        massimo = max(massimo,sum);
        prefix.push_back(sum);
    }
    
    return massimo;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    vi nums;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        nums.push_back(x);
    }
    
    auto ris = largestAltitude(nums);

    cout << ris;
    
    return 0;
}