class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #set pointers at the start and end of the bar graph
        l, r = 0, len(heights) -1
        res = 0

        #while the 2 pointers dont cross
        while l < r:

            #set result to the max between result and area of the square
            res = max(res, ((r - l) * min(heights[r], heights[l])))

            #increment left if the left value is lower than right
            if heights[l] < heights[r]:
                l +=1
            #decrement right if right value is lower than left
            elif heights[r] <= heights[l]:
                r-=1
            
        return res
