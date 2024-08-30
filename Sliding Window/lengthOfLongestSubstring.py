class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize a set to help find dups
        charSet = set()

        l = 0
        res = 0

        #keep the right pointer shifting throughout length
        for r in range(len(s)):

            #while there is a duplicate in the set then remove the left pointer character and shift
            #left pointer
            while s[r] in charSet: #while loop is used since it continously checks for character is charset
                charSet.remove(s[l])
                l +=1
            #add right character onto the substring 
            charSet.add(s[r])
            res = max(res, r-l+1)
        
        return res
            
