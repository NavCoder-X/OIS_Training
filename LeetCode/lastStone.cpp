#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> pq;

    for (int i = 0; i < stones.size(); i++)
    {
        pq.push(stones[i]);
    }

    while (pq.size() > 1)
    {
        int x, y;
        x = pq.top();
        pq.pop();
        y = pq.top();
        pq.pop();
        if(x != y) pq.push(x-y);
    }
    
    return (pq.size()) ? pq.top() : 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;
    vi stones(n);

    for (int i = 0; i < n; i++)
    {
        cin >> stones[i];
    }
    
    auto ris = lastStoneWeight(stones);
    cout << ris;
    return 0;
}