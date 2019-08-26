# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        s = [root]
        while s:
            node = s.pop()
            if node:
                if L <= node.val <= R:
                    result += node.val
                if L < node.val:
                    s.append(node.left)
                if node.val < R:
                    s.append(node.right)
        return result

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
res = Solution().rangeSumBST(root, 1, 2)
print(res)