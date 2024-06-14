# HERE IS THE SOLUTION WHICH WAS DONE IN FIRST ATTEMPT, WITHOUT OPTIMIZING RUNTIME - Time Complexity = O(n^2), Space Complexity = O(n)
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


#SOLUTION WITH OPTIMIZING RUNTIME - Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #init hashmap (map value to index)
        prevMap = {}

        #loop through the list with 2 vars (index and value)
        for i, n in enumerate(nums):

            #calculate difference and see whether difference is in hashMap
            diff = target - n
            if diff in prevMap:
                return[prevMap[diff], i] #return value and index
            
            #if value isn't in hashmap, update hashmap
            prevMap[n] = i
