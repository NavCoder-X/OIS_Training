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

bool isValid(vi &books,ll t,int k){
    ll sum = 0;
    int i = 0, j = 0;
    for (j = 0; j < k; j++)
        sum += books[j];
    if(sum <= t) return true;
    
    while (j < books.size())
    {
        sum -= books[i++];
        sum += books[j++];
        if(sum <= t) return true;
    }
    
    return false;
}

int solve(vi & books,ll t){
    int l = 0, r = books.size();
    int answer = 0;
    while (l <= r)
    {
        int mid = l + (r-l)/2;
        if(isValid(books,t,mid)){
            answer = mid;
            l = mid+1;
        }else r = mid-1;
    }
    
    return answer;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    ll t;
    cin >> n >> t;

    vi nums(n);
    for(int i = 0;i < n;i++){
        cin >> nums[i];
    }

    auto ris = solve(nums,t);
    cout << ris << endl;
    return 0;
} 