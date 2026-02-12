#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vi nearestSmaller(vi &nums){
    vi ris(nums.size());
    stack<int> s;

    for (int i = nums.size()-1; i >= 0; i--)
    {
        while (!s.empty() && nums[i] < nums[s.top()])
        {
            ris[s.top()] = i+1;
            s.pop();
        }
        s.push(i);
    }
   
    return ris;
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

    auto ris = nearestSmaller(nums);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}