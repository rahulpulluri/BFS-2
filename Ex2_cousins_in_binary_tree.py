# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(N), for the queue used in level-order traversal
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque()
        q.append((root, None))  # (node, parent)

        while q:
            size = len(q)
            x_parent = None
            y_parent = None

            for _ in range(size):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            # Check after each level
            if x_parent and y_parent:
                return x_parent != y_parent  # True if different parents
            if x_parent or y_parent:
                return False  # Found only one of x or y at this level

        return False

# -----------------------------------------------------------------------------
# Alternative BFS using two queues
# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(N), due to the two queues used in level-order traversal

#         if not root:
#             return False
#         q = deque()
#         pq = deque()  # parent queue
#         q.append(root)
#         pq.append(None)

#         while q:
#             size = len(q)
#             x_parent = None
#             y_parent = None

#             for _ in range(size):
#                 node = q.popleft()
#                 parent = pq.popleft()

#                 if node.val == x:
#                     x_parent = parent
#                 if node.val == y:
#                     y_parent = parent

#                 if node.left:
#                     q.append(node.left)
#                     pq.append(node)
#                 if node.right:
#                     q.append(node.right)
#                     pq.append(node)

#             if x_parent and y_parent:
#                 return x_parent != y_parent
#             if x_parent or y_parent:
#                 return False

#         return False

# -----------------------------------------------------------------------------
# Alternative DFS approach (recursive, single-pass)
# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(H), where H is the height of the tree (due to recursion stack)

#         self.x_parent = None
#         self.y_parent = None
#         self.x_depth = -1
#         self.y_depth = -1

#         def dfs(node, parent, depth):
#             if not node:
#                 return

#             if node.val == x:
#                 self.x_parent = parent
#                 self.x_depth = depth
#             elif node.val == y:
#                 self.y_parent = parent
#                 self.y_depth = depth

#             if self.x_parent and self.y_parent:
#                 return

#             dfs(node.left, node, depth + 1)
#             dfs(node.right, node, depth + 1)

#         dfs(root, None, 0)

#         return (self.x_depth == self.y_depth) and (self.x_parent != self.y_parent)
