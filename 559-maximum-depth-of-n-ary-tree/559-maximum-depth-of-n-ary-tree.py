"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
    
        def dfs(root):
            height = 0
            if not root:
                return 0
            for node in root.children:
                height = max(dfs(node), height)
                
            return height + 1
        return dfs(root)