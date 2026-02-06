#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

/* Soluzione: tecnica Sliding window di 3
   quando rimuovo due caratteri consecutivi da una stringa generreo la stessa sotto stringa solo e solo se quando rimuvo due caratteri
   vicini il suo sucessivo è uagule al primo carattere che sto rimuovendo, in quanto se poi rimuovo i prossimi due ritrovo lo stesso carattere nella stessa posizione,
   es: abacac
    |ab|acac -> acac
    a|ba|cac -> acac 
   e vale cosi anche per "cac".
   il problema garantisce che la stringa e almeno lunga 3 , ci sara sempre almeno 1 soluzione*/
   
int Solve(string &s){
    int sets = 1;

    int i = 0;
    int j = 2;
    while(j < s.size()){
        if(s[i++] != s[j++]) sets++;
    }

    return sets;
}
 
int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        string s;
        cin >> n;
        cin >> s;

        // solution Sliding Window
        auto sets = Solve(s);
        cout << sets << endl;
    }
    
    
    return 0;
}