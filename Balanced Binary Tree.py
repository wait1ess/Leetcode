# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 高度平衡二叉树是每一个结点的两个子树的深度差不能超过1
# 一个求各个点深度的函数，然后对每个节点的两个子树来比较深度差，O(NlgN)
class Solution:

    def Height(self, root):           # 计算（子）二叉树高度的函数
        if root == None:              # 树为空时，高度为0
            return 0
        # 递归求解
        # 树的高度 = max(左子树高度，右子树高度)+1
        return max( self.Height( root.left ), self.Height( root.right ) ) + 1
    
    def isBalanced(self, root): # 递归求解每个节点的左右子树的高度差
        if root  == None:
            return True
        if abs( self.Height( root.left ) - self.Height( root.right ) ) <= 1:  # 如果有大于1的，则return False
             return self.isBalanced( root.left ) and self.isBalanced( root.right )  #如果高度差小于等于1，则继续递归求解。
        else:
            return False
        
