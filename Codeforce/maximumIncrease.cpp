#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int maxIncrese(vi & nums){
    if(nums.size() <= 0) return 0;

    int c = 1;
    int massimo = 1;
    for (int i = 1; i < nums.size(); i++)
    {
        if(nums[i] > nums[i-1]) c++;
        else c = 1;
        massimo = max(massimo,c);
    }
    
    return massimo;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;
    vi nums(n);

    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    
    auto ris = maxIncrese(nums);
    cout << ris << endl;
    return 0;
}