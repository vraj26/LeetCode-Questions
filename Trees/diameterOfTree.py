# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #this is a global member which I can use within the function itself
        self.res = 0

        #returns the height of the tree
        def dfs (curr):
            if not curr: #if the tree is empty then return 0 as the height
                return 0

            #find the hright of the left and right subtree by calling it recursively
            left = dfs(curr.left)
            right = dfs(curr.right)


            #set the result between itself and the combination of left and right (aka the diameter)
            self.res = max(self.res, left + right)

            #THIS ONE acc returns the height (add 1 to account for current node)
            return 1 + max(left, right)

        #call the function on the tree and return the result
        dfs(root)
        return self.res


