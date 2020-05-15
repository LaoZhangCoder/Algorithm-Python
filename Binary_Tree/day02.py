class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftDepth = self.maxDepth(root.left) + 1
        rightDepth = self.maxDepth(root.right) + 1
        return leftDepth if leftDepth > rightDepth else rightDepth
