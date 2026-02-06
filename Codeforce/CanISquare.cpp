#include <iostream>
#include <string>
#include <cmath>
using namespace std;

/* Soluzione: usare una funzione di libreria per precisione migliore e non andare in overflow
    stare attenti al over flow
    necessita di precisione
   Soluzione alternativa: Binary Search con double, devi vedertela anche con i controlli tra float e long long*/
string perfetSquare(long long n){
    if (n < 1) return "NO";
    long long r = (long long) sqrtl((long double)n);
    return (r * r == n) ? "YES" : "NO";
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        long long n, x, sum = 0;
        cin >> n;
        for (int j = 0; j < n; j++){
            cin >> x;
            sum += x;
        }
        cout << perfetSquare(sum) << endl;
    }
    return 0;
}