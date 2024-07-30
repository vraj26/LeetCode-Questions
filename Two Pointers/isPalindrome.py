class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize an empty string to hold the alphanumeric characters
        newStr = ""

        # Iterate through each character in the input string
        for c in s:
            # Check if the character is alphanumeric
            if c.isalnum():
                # If it is, convert it to lowercase and add it to the new string
                newStr += c.lower()
        
        # Check if the new string is equal to its reverse
        return newStr == newStr[::-1]
