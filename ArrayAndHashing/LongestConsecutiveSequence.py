#Time: O(n)
#Space: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the input list to a set for O(1) lookup time
        numSet = set(nums)
        longest = 0  # Variable to store the length of the longest consecutive sequence

        for n in nums:
            # Check if the current number is the start of a sequence
            # It's a start if the number before it (n-1) is not in the set
            if (n - 1) not in numSet:
                length = 0  # Initialize the length of the current sequence

                # Keep incrementing length while the next consecutive number exists in the set
                while (n + length) in numSet:
                    length += 1
                
                # Update the longest sequence if the current sequence is longer
                longest = max(length, longest)
        
        # Return the length of the longest consecutive sequence found
        return longest
