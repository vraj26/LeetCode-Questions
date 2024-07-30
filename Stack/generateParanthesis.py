class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Stack to build current combination of parentheses
        stack = []
        # List to store all valid combinations
        res = []

        def backtrack(openN, closedN):
            # Base case: if we have used n open and n closed parentheses,
            # we have a valid combination
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # If we can add an open parenthesis, do so
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()  # Backtrack by removing the last added parenthesis
            
            # If we can add a closed parenthesis, do so
            # We can add a closed parenthesis if there are more open than closed ones
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()  # Backtrack by removing the last added parenthesis
        
        # Start the backtracking with 0 open and 0 closed parentheses
        backtrack(0, 0)
        return res
