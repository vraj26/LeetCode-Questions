#Time Complexity: O(n), Space Complexity: O(1) (it is considered that the result array doesn't contribute to extra space)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #init output array of 1s w/ same length as nums
        result = [1] * len(nums)

        #init prefix value and loop through nums and at each position i, set that to prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix

            #update prefix value
            prefix *= nums[i]

        #postfix pass
        postfix = 1
        for i in range(len(nums) -1, -1, -1):

            #multiplies prefix with postfix
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
