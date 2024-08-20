class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left is byuing, right is selling
        maximum = 0

        while r < len(prices):
            #is it profitable?
            if prices[l] < prices[r] :

                #calculate the profit and set maximum to the max between itself and profit 
                profit = prices[r] - prices[l] 
                maximum = max(maximum, profit) 
                
            else:

                #setting left pointer to next lowest value which will be at right pointer
                l = r
            
            #incr right pointer by 1 after each iteration to check for new maxProfit
            r += 1
            
            
        return maximum
