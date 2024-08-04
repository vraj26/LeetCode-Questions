class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Initialize result list
        nums.sort()  # Sort the input array

        for i, a in enumerate(nums):
            # Skip duplicate values for 'a' to avoid duplicate triplets
            if i > 0 and a == nums[i-1]:
                continue
            
            # Set up two pointers for the remaining two numbers
            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # Sum too large, decrement right pointer
                elif threeSum < 0:
                    l += 1  # Sum too small, increment left pointer
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])

                    l += 1  # Move left pointer

                    # Skip duplicates for 'l'
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        return res
