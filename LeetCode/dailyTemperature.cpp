#include <iostream>
#include <vector>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

vector<int> dailyTemperatures(vector<int> &temperatures){
    vector<int> ris(temperatures.size());
    stack<int> s;

    for (int i = 0; i < temperatures.size(); i++)
    {
        while (!s.empty() && temperatures[s.top()] <= temperatures[i])
        {
            ris[s.top()] = i - s.top();
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
    vi temperature(n);

    for (int i = 0; i < n; i++)
    {
        cin >> temperature[i];
    }

    auto ris = dailyTemperatures(temperature);
    for (auto n: ris){
        cout << n << ' ';
    }
    return 0;
}