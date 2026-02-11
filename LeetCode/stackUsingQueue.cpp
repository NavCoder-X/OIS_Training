#include <iostream>
#include <vector>
#include <queue>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

class MyStack {
public:
    queue<int> q;
    MyStack() {
        
    }
    
    void push(int x) {
       int n = q.size();
       q.push(x);
       for (int i = 0; i < n; i++)
       {
            int a = q.front();
            q.pop();
            q.push(a);
       }
    }
    
    int pop() {
        int x = q.front();
        q.pop();
        return x;
    }
    
    int top() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
};

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    MyStack s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    return 0;
}