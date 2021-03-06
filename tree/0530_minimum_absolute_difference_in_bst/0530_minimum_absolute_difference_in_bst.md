530. Minimum Absolute Difference in BST


Easy


Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

```


## 方法


```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type state struct{
    minDiff , previous int
}

func getMinimumDifference(root *TreeNode) int {
    st:=state{1024,1024}
    search(root, &st)
    return st.minDiff
}

// NOTICE: BST 的递归遍历方法
func search(root *TreeNode, st *state){
    if root == nil{
        return
	}

    search(root.Left, st)
    
    newDiff:=diff(st.previous, root.Val)
    if st.minDiff> newDiff{
        st.minDiff = newDiff
    }
    
	st.previous = root.Val

    search(root.Right, st)
}

func diff(a, b int) int{
    if a > b{
        return a - b
    }
	return b - a
}
```



```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorderTraversal(root, prev, result):
            if not root:
                return (result, prev)

            result, prev = inorderTraversal(root.left, prev, result)
            if prev: result = min(result, root.val - prev.val)
            return inorderTraversal(root.right, root, result)

        return inorderTraversal(root, None, float("inf"))[0]
```