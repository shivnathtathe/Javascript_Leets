class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_depth = 0
        current_stack = [(root, 1)]
        
        while current_stack:
            node, depth = current_stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                current_stack.append((node.left, depth + 1)) 
            if node.right:
                current_stack.append((node.right, depth + 1))
        return max_depth
