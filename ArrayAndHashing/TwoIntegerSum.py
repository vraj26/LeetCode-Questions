# HERE IS THE SOLUTION WHICH WAS DONE IN FIRST ATTEMPT, WITHOUT OPTIMIZING RUNTIME
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #init flag to false
        flag = False

        #loop through the list and compare index with every other index
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                #in the first match set flag to true
                if nums[i] + nums[j] == target:
                    flag = True
                
                #return pair on indexes
                if flag:
                    return i, j


#SOLUTION WITH OPTIMIZING RUNTIME
