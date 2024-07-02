#Time: O(n), Space: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #hashmap initialized such that there are no edge cases

        #loop through the strs list as s being individual strings
        for s in strs:
            count = [0] * 26 #init empty array of 26 0s, each representing count of alphabet
            
            #loop through the strings, c being individual letter
            for c in s:
                count[ord(c) - ord('a')] += 1

            #the key being the count of letters and values being anagrams
            result[tuple(count)].append(s)

        return result.values()

