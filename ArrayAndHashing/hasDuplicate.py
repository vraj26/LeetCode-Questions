class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for n in range(len(nums)):
            for j in range(n+1, len(nums)):
                if nums[n] == nums[j]:
                    return True
         return False

#ANOTHER WAY OF DOING THIS SIMILAR TO isAnagram:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hashmap = {};

         for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

         for n in hashmap:
            if hashmap[n] > 1:
                return True
        
         return False
