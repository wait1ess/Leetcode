# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None: return []
        def DPS(node,output):
            output.append(node.val)
            if node.left:
                DPS(node.left,output)
            if node.right:
                DPS(node.right,output)
        output=[]
        DPS(root,output)
        return output


            
