#include <vector>
#include <algorithm>
using namespace std;

int trova_massimo(int N, vector<int> V) {
    return *max_element(V.,V.end());
}
