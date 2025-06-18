#include <vector>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> indices;
        for (int x = 0; x < (nums.size() - 1); x++) {
            for (int i = x + 1; i < nums.size(); i++) {
                if((nums[x] + nums[i]) == target) {
                    indices.push_back(x);
                    indices.push_back(i);
                    return indices;
                }
            }
        }
        return indices;
    }
};