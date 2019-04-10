# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#一棵树的前序遍历，在每一层一定都先遍历到最左边那个结点
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num=1
        self.max=1
        self.res=TreeNode(root.val)
        def search(root,num):
            if root.left:search(root.left,num+1)
            if root.right:search(root.right,num+1)
            if num>self.max:
                self.res=root
                self.max=num
 
        search(root,num)
        return self.res.val
