# Approach:
# 1. Use Breadth-First Search (BFS) to traverse the tree level by level using a queue.
# 2. For each level, track the nodes in the queue, adding their values to the current level list.
# 3. Append the current level's values to the result list after processing all nodes at that level.

# Time Complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.
# Space Complexity: O(w), where w is the maximum width of the tree (size of the queue at its largest).
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the root is None, return an empty list
        if not root:
            return []

        # Initialize a queue to perform BFS and a result list
        queue = deque([root])
        result = []

        # Perform BFS
        while queue:
            # Track the size of the current level
            level_size = len(queue)
            current_level = []

            # Traverse all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Add the left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the current level to the result
            result.append(current_level)

        return result
