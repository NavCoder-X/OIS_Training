#include <iostream>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

// IRRISOLTO : SPACE LIMITI EXCECEDED

template<typename T>
using order_set = tree<
    T,
    null_type,
    less<T>,
    rb_tree_tag,
    tree_order_statistics_node_update>;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
 
    int n, q;
    cin >> n >> q;
    int id = 0;
    
    order_set<pair<int,int>> os;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        os.insert({x, id++});
    }

    for (int i = 0; i < q; i++)
    {
        int query;
        cin >> query;
        if (query < 0) {
            auto it = os.find_by_order(-query - 1);
            os.erase(it);
        } else {
            os.insert({query, id++});
        }
    }

    if (os.size() == 0) cout << 0 << endl;
    else cout << (*os.begin()).first << endl;

    return 0;
}