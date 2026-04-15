# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        max_width = 0
        # queue holds pairs of (node, index) where index is the position
        q = deque([(root, 0)])

        while q:
            level_size = len(q)
            first_index = q[0][1]
            last_index = q[-1][1]
            # Update the maximum width based on current level
            max_width = max(max_width, last_index - first_index + 1)

            # Process all nodes in the current level
            for _ in range(level_size):
                node, index = q.popleft()
                # Enqueue children with their corresponding indices
                if node.left:
                    q.append((node.left, 2 * index))
                if node.right:
                    q.append((node.right, 2 * index + 1))

        return max_width