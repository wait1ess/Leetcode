# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result=[]
        queue=collections.deque()
        queue.append(root)
        # visited=set(root)

        while queue:
            level_size=len(queue)   # 当前层的长度
            current_level=[]
            for _ in range(level_size):
                node=queue.popleft()
                current_level.append(node.val)      # 当前层的元素
                
                if node.left:                       # 下一层的元素加入queue
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result
                    
                    
