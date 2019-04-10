# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q) :
        while root:                                    
            if p.val<root.val>q.val:                  # 若当前节点大于两目标节点，往左子树递归
                root=root.left
            elif p.val>root.val<q.val:                # 若当前节点小于两目标节点，往右子树递归
                root=root.right
            else:                                     # 直至节点到达一个位置 其值小于一个目标而大于另一个目标
                return root
