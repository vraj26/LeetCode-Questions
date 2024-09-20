class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #make a pointer point at 1 and maximum value of piles
        l, r = 1, max(piles)
        res = r

        #loop through initializing k as the "eating rate"
        while l <= r:
            k = (l+r) // 2
            totalTime = 0 #init totalTime 

            #loop through all the bananas in piles and calculate the time taken to eat those bananas
            for p in piles:
                totalTime += math.ceil(float(p) / k)

            #if the totalTime it takes to eat bananas is less than h, and try a lower k value 
            if totalTime <= h:
                res = k
                r = k-1
            else: #if totalTime is is too big (bigger than k) try a higher eating value
                l = k+1
            
        #return the result
        return res


