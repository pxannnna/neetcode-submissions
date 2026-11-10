# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # do dfs to the very last node
        # no node.right or node.left
        # backtrack
        # choose which path is give you more left/right
        # if parent node is making it worse (sumsofar + parent.) < sumsofar: return rightsum+leftsum
        curr = TreeNode()
        curr = root
        currmaxsum = 0
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            leftsum = max(dfs(node.left), 0)
            rightsum = max(dfs(node.right), 0)


            res = max(res, node.val + leftsum + rightsum)

            return node.val + max(rightsum, leftsum) # include parent, store max
        dfs(root)
        return res


            





        