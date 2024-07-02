class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #init hashmap and array with same length as nums 
        hashmap = {}
        arr = [[] for i in range(len(nums) +1)]

        #count each occurence of each number
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        #loop through hashmap and append the number as count as index
        for num, count in hashmap.items():
            arr[count].append(num) #the value num occurs count number of times
        
        res = []

        #loop through the array in descending order, loop through the sublists and append n
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)

                #if the length matches k then return result
                if len(res) == k:
                    return res
