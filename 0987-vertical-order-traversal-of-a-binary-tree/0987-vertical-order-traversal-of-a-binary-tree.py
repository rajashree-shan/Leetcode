# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list)
        q = deque([(root, 0, 0)])   # (node, row, col)

        while q:
            node, row, col = q.popleft()

            col_map[col].append((row, node.val))

            if node.left:
                q.append((node.left, row + 1, col - 1))

            if node.right:
                q.append((node.right, row + 1, col + 1))

        res = []

        for col in sorted(col_map):
            temp = sorted(col_map[col])   # sorts by row, then value
            res.append([val for row, val in temp])

        return res