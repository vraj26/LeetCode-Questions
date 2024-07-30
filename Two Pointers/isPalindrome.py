#Time: O(n), Space: O(n)
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



#Time: O(n), Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers, left at the start and right at the end of the string
        left, right = 0, len(s) - 1

        # Loop until the two pointers meet
        while left < right:
            # Move the left pointer to the right until an alphanumeric character is found
            while left < right and not self.alphaNum(s[left]):
                left += 1

            # Move the right pointer to the left until an alphanumeric character is found
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            # Compare the characters at the left and right pointers (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move the pointers towards the center
            left, right = left + 1, right - 1

        # If all characters matched, the string is a palindrome
        return True

    def alphaNum(self, c):
        # Check if a character is alphanumeric using its ASCII value
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
