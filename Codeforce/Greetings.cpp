#include <iostream>
#include <algorithm>
#include <vector>

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
using namespace std;

template<typename T>
using ordered_set = tree<
    T,
    null_type,
    less<T>,
    rb_tree_tag,
    tree_order_statistics_node_update>;


/* Soluzione: ordino tutte le persone per istante iniziale dal piu avanti al indietro
    la persona che si trova alla poszione piu avanti non saluta mai nessuno e quindi possiamo poratrla subito al suo istante finale
    tutte le latre persone potrebbero salutarlo se il loro istante finale e maggiore de suo , quindi grazie al ordered set
    computiamo quante persone ciascuna persona puo salutare prima di raggiungere il suo traguardo in complessita logN
    tutto cio e possibile perche tutti i valori sono distinti e quindi mettibili in un set, ricordandosi di portare la persona di cui abbiamo calcolato i saluti al suo istante finale mettendolo nel set*/
long long Solve(vector<pair<long long,long long>>& persone){
    auto f = [](const pair<long long,long long> &a,const pair<long long,long long> &b){
        return a.first > b.first;
    };
    sort(persone.begin(),persone.end(),f); // ordino per istante

    long long saluti = 0;

    ordered_set<long long> record;
    record.insert(persone.begin()->second);
    persone.erase(persone.begin());

    for (auto & p: persone){
        // cout << p.first << " " << p.second << endl;
        saluti += record.order_of_key(p.second);
        record.insert(p.second);
        // persone.erase(p.first);
    }       

    return saluti;
}
 
int main() {
    int t;
    long long n, a, b;
    cin >> t;
    
    for (int i = 0; i < t; i++)
    {
        // lettura
        vector<pair<long long,long long>> persone;
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> a >> b;
            persone.push_back(pair(a,b));
        }

        // soluzione
        auto saluti = Solve(persone);
        cout << saluti << endl;
    }
    
    return 0;
}
