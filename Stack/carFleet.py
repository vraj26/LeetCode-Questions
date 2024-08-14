class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create pair using list comprehension:
        pair = [[pos, s] for pos, s in zip(position, speed)]

        #initialize stack
        stack = []

        #loop through sorted pair backwards
        for pos, s in sorted(pair)[::-1]:

            #append the time it takes for respective car to reach target
            stack.append((target-pos) / s)

            #if there is 2 or more cars AND the time it takes for the latter car is faster than the car after it
            #then pop from the stack to make it a car fleet (use the car after as reference point)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        #return the length of the stack
        return len(stack)
