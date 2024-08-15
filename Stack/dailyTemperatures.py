class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #consists of 0s using list comprehension

        stack = [] #will contain [temm, index]

        #loop through containing index and value
        for i, t in enumerate(temperatures):
            
            #check if stack exists and whether CURRENT temperature is greater than 
            #the lowest temperature (which in this case is the top of stack)
            while stack and stack[-1][0]< t:

                #pop if true, and compute how many days it takes for higher temp
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i-stackIndex

            stack.append((t, i))

        return res
