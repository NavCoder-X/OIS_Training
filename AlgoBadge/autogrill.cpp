#include <set>
#include <algorithm>
using namespace std;
set<long long> s;

void inizia() {
    return;
}

void apri(long long p) {	
	s.insert(p);
}

void chiudi(long long p) {	
	s.erase(p);
}

long long chiedi(long long p) {
	if (s.size() == 0) return -1;
    auto it = s.lower_bound(p);
    if (it == s.end()) return *s.rbegin();
    if (*it == p) return p;
    if (it == s.begin()) return *it;
    
	long long a = *it, b = *prev(it);
	long long aDif = abs(p-a), bDif = abs(b-p);
	if (aDif == bDif) return a;
	return aDif < bDif ? a : b;
}
