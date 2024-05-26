class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //first sort the list
        int temp;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[i] > nums[j]){
                    temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }

        //check if there are any duplicates
        for(int v = 0; v < nums.size(); v++){
            if(nums[v] == nums[v+1]){
                return true;
            } 
        }
        return false;
        
    }
};
