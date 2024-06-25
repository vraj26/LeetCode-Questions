class Solution:
    #Time: O(n^2), Space: O(1)
    def hasDuplicate(self, nums: List[int]) -> bool:
        #check each element with another and see if it matches
         for n in range(len(nums)):
            for j in range(n+1, len(nums)):
                if nums[n] == nums[j]:
                    return True
         return False

#ANOTHER WAY OF DOING THIS SIMILAR TO isAnagram: Time: O(n) Space: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #init hashmap
         hashmap = {}

        #loop through the list and add each occurence of the number (the key will be the # in nums, and value would be # of occurences)
         for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        #loop through the hashmap and see if there is a number occurring more than once
         for n in hashmap:
            if hashmap[n] > 1:
                return True
        
         return False
