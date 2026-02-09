#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, i, j;
    bool trovato = 1;
    
    for (i = 1; i < 6 && trovato; i++)
    {
        for (j = 1; j < 6 && trovato; j++)
        {
            cin >> n;
            if(n == 1) trovato = 0;
        }
    }
    i--;
    j--;
    int ris = abs(3-i) + abs(3-j);

    cout << ris << endl;
    return 0;
}