#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

void Hanoi(int blocchi,stack<int> &src,stack<int> &temp,stack<int> &dest){
    if(blocchi > 0){
        // muovo tutti blocchi -1 da src a temp
        Hanoi(blocchi-1,src,dest,temp);
        // adesso tutti i blocchi sono in temp quindi muovo il blocco in dest
        dest.push(src.top());
        src.pop();
        // muovo n-1 blocchi da temp a dest
        Hanoi(blocchi-1,temp,src,dest);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> src, temp, dest;

    int blocchi;
    cin >> blocchi;

    for (int i = blocchi; i > 0; i--)
    {
        src.push(i);
    }

    Hanoi(blocchi,src,temp,dest);
    
    while (!dest.empty())
    {
        cout << dest.top() << endl;
        dest.pop();
    }
    
    return 0;
}