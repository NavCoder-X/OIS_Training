// Singh Navjot
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> sets;
vector<int> setAttuale;
void genera(vector<int> & nums,int depth){
    if(depth == nums.size()){
        sets.push_back(setAttuale);
        return;
    }

    setAttuale.push_back(nums[depth]);
    genera(nums,depth+1);
    setAttuale.pop_back();
    genera(nums,depth+1);
}

vector<vector<int>> subsets(vector<int>& nums) {
    genera(nums,0);
    return sets;
}
 
int main() {
    vector<int> nums = {1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6};
    auto x = subsets(nums);
    
    for (auto v: x){
        for (auto n: v){
            cout << n << ' ';
        }
        cout << endl;
    }
    
    return 0;
}