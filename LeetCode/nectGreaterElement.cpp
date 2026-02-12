#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    // trasformo nums1 in una map di pair<val,indice>
    unordered_map<int,int> s;
    vector<int> ris(nums1.size(),-1);
    stack<int> ms; // monotonic stackù

    for (int i = 0; i < nums1.size(); i++)
    {
        s[nums1[i]] = i;
    }

    // scorro ogni nums2
    for (auto n: nums2){
        while(!ms.empty() && n > ms.top())
        {
            auto it = s.find(ms.top());
            if(it != s.end()){
                ris[s[ms.top()]] = n;
            }
            ms.pop();
        }
        ms.push(n);
    }
    
    return ris;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, m;
    cin >> n >> m;
    vi nums1(n), nums2(m);
    for (int i = 0; i < n; i++)
    {
        cin >> nums1[i];
    }
    for (int i = 0; i < m; i++)
    {
        cin >> nums2[i];
    }

    auto ris = nextGreaterElement(nums1,nums2);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}