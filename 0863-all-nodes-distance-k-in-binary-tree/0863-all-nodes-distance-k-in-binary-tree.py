# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque
        parent={}
        def build(node,par):
            if not node:
                return
            parent[node]=par
            build(node.left,node)
            build(node.right,node)
            return
        build(root,None)

        q=deque([target])
        visited = set([target])
        dist = 0

        while q:
            level=len(q)
            if dist == k:
                return [node.val for node in q]
            for i in range(level):
                node=q.popleft()

                for j in node.left,node.right,parent[node]:
                    if j and j not in visited:
                        visited.add(j)
                        q.append(j)

            dist += 1

        return []

