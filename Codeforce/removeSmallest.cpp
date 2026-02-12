#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

string can(vi &nums){ 
    sort(nums.begin(),nums.end());
    stack<int> s; 
     
    for(int i = 0;i < nums.size();i++){
        if(!s.empty() && nums[i] >= s.top()){
            if(nums[i] - s.top() <= 1) s.pop();
        }
        s.push(nums[i]);
    }
    
    return (s.size() <= 1) ? "YES" : "NO";
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
        vi nums(n);

        for (int j = 0; j < n; j++)
        {
            cin >> nums[j];
        }

        auto ris = can(nums);
        cout << ris << endl;
    }
    
    return 0;
}