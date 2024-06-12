class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the lengths dont match then return false
        if len(s) != len(t):
            return False

        #init hashmaps
        countS, countT = {}, {}

        #loop through the strings and count each occurence
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #if key doesn't exist, return 0
            countT[t[i]] = 1 + countT.get(t[i], 0) #if key doesn't exist, return 0
        
        #loop through hashmaps and compare occurences
        for n in countS:
            if countS[n] != countT.get(n, 0):
                return False
        
        return True
