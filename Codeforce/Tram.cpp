#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n;
    cin >> n;
    int massimo = 0;
    int sum = 0;

    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;

        sum -= a;
        sum+= b;
        massimo = max(massimo,sum);
    }

    cout << massimo;
    
    return 0;
}