# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root==None:return[]
        answer=[]
        self.k=k
        self.InOrder(root,answer)
        return answer[self.k-1]
    def InOrder(self,root,answer):
        if len(answer)>=self.k: return
        if root:
            if root.left:self.InOrder(root.left,answer)
            answer.append(root.val)
            if root.right:self.InOrder(root.right,answer)
