# Time Complexity: O(N), where N is the number of nodes in the binary tree
# Space Complexity: O(N), for the queue used in BFS
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  
        # BFS approach using queue
        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current_node = queue.popleft()

                # Add the rightmost element at the current level
                if i == level_size - 1:
                    result.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return result

        # ------------------------------------------------------------
        # DFS-based Recursive Approach (alternative)
        # Time Complexity: O(N)
        # Space Complexity: O(H), where H is the height of the tree (recursion stack)
        
        # result = []
        #
        # def dfs(node: Optional[TreeNode], level: int):
        #     if not node:
        #         return
        #
        #     if level == len(result):
        #         result.append(node.val)
        #
        #     dfs(node.right, level + 1)
        #     dfs(node.left, level + 1)
        #
        # dfs(root, 0)
        # return result
