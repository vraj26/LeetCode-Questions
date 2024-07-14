class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #init stack
        stack = []

        #loop through input array
        for item in tokens:

            #if its addition or multiplication simply perform operation (order doesn't matter)
            if item == "+":
                stack.append(stack.pop() + stack.pop())
            elif item == "*":
                stack.append(stack.pop() * stack.pop())

            #if its subtraction or addition, be sure to take the second character and treat it as primary when performing operation
            elif item == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif item == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            #if its not an operation and append onto the stack
            else:
                stack.append(int(item))
        #return the last element within the stack
        return stack[0]
