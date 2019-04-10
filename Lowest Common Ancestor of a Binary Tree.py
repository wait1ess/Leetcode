# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 在二叉树中来搜索p和q，然后从路径中找到最后一个相同的节点即为父节点
# 递归实现
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):

            # 看当前结点是否为空，若为空则直接返回空
            if not current_node:
                return False
            
            # 否则的话就对其左右子结点分别调用递归函数
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            # 判断是否为目标节点的其中一个
            mid = current_node == p or current_node == q
            
            # 若该节点满足左右子树或当前节点是目标节点，则将当前节点更新为候选祖先
            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
        
