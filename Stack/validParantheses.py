#Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        #init stack and map each closing bracket to opening
        stack = []
        closeToOpen = {")" : "(",
                       "]" : "[",
                       "}" : "{"}

        #loop through input
        for bracket in s:

            #if the bracket is a closing bracket then...
            if bracket in closeToOpen:

                #if the stack is not empty and the value at top of stack is the same as the matching open parantheses..
                if stack and stack[-1] == closeToOpen[bracket]:

                    #pop from the stack, else the string is invalid
                    stack.pop()
                else:
                    return False
            
            #if the bracket is opening bracket then simply append
            else:
                stack.append(bracket)
        
        #If the stack is empty return true, otherwise return false
        return True if not stack else False
