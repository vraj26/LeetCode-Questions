class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #init the left and right pointers
        l, r = 0, len(numbers) - 1

        #only loop through when left pointer is ALWAYS left of the right pointer
        while l < r:

            #hold the current sum in var
            curr_sum = numbers[l] + numbers[r]


            #if the current sum is equal to teh target then return using 1-indexed
            if (curr_sum) == target:
                return [l +1, r +1]

            #if the current sum is less then target then increment left, if its greater then decrement right
            elif curr_sum < target:
                l = l+1
            else:
                r = r-1
