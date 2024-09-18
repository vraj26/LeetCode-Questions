# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #check the base case
        if not root: #if the root is null then return Null (tree doesn't exist)
            return None

        #swap the children
        tmp = root.left #left child stored in temp
        root.left = root.right #swap left child and make it the right child
        root.right = tmp #make the right child tmp (which is the left child )
        
        #recursively call this function on both the left subtree and the right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        #return the new tree
        return root
