# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s:
            return False
        if not t: 
            return False

        if self.SameTree(s,t):
            return True
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))

    def SameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.SameTree(s.left, t. left) and 
                self.SameTree(s.right, t.right))
        return False
