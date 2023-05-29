class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        nums.erase(remove_if(nums.begin(), nums.end(), [val](auto x) -> bool { return x == val; }), nums.end());
        
        
        return nums.size();
    };
};