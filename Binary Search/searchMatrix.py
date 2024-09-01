class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #initialize the rows and cols for initial binary search
        rows, cols = len(matrix), len(matrix[0])

        #set the "pointers" to the specified 
        topRow, botRow = 0, rows-1

        #while making sure the pointers don't cross
        while topRow <= botRow:
            #compute the "row" midpoint
            row = (topRow + botRow) // 2

            #if target value is greater than the largest value in that row, then 
            #shift the topRow pointer down (aka, shift to a row with larger numbers)
            if target > matrix[row][-1]:
                topRow = row + 1
            
            #if the target is less than the lowest value of that row, then shift
            #the bottomRow pointer up one (aka shift to lower numbers)
            elif target < matrix[row][0]:
                botRow = row - 1
            
            #if neither of the if statements evaluate, this means that 
            #the target is within the specified row already
            else:
                break
        

        #this means none of the rows contain teh target value, so return false
        if not (topRow <= botRow):
            return False
        


        #row which the second binary search will be ran
        row = (topRow + botRow) // 2

        #set the pointers for the second binary search 
        l, r = 0, cols - 1

        while l <= r:
            #compute midpoint for second binary search
            m = (l+r) // 2

            #if the target is greater than the midpoint, shift left pointer
            if target > matrix[row][m]:
                l = m+1
            
            #if the target is less than the midpoint, shift the right pointer
            elif target < matrix[row][m]:
                r = m-1
                
            #else return True
            else:
                return True
        return False
