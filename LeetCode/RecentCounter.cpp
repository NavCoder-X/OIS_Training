#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

class RecentCounter {
public:
    queue<long long> requests;
    long long offset = 3000;
    RecentCounter() {

    }
    
    int ping(int t) {
        requests.push(t);
        int target = t - offset;
        while (requests.front() < target) requests.pop();
        return requests.size();
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    RecentCounter rc;
    cout << rc.ping(1) << endl;
    cout << rc.ping(100) << endl;
    cout << rc.ping(3000) << endl;
    cout << rc.ping(3001) << endl;
    return 0;
}