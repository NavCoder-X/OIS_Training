#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int calPoints(vector<string>& operations) {
    if(operations.size() <= 0) return 0;
    stack<int> s;
    int sum = 0;
    int a, b;

    for (auto &o: operations){
        if(o == "D"){
            a = s.top();
            s.push(a*2);
            sum += s.top();
        }else if(o == "C"){
            sum -= s.top();
            s.pop();
        }else if(o == "+"){
            a = s.top();
            s.pop();
            b = s.top();
            s.push(a);
            sum += a+b;
            s.push(a+b);
        }else{
            sum += stoi(o);
            s.push(stoi(o));
        }
    }

    return sum;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    vector<string> ops;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string x;
        cin >> x;
        ops.push_back(x);
    }
    
    auto ris =calPoints(ops);
    cout << ris;
    return 0;
}