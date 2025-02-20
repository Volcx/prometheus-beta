class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_minimum_path_sum(root):
    """
    Find the path with the minimum sum from the root to any leaf in a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        int: The minimum path sum from root to a leaf
    
    Raises:
        ValueError: If the root is None
    """
    if root is None:
        raise ValueError("Tree cannot be empty")
    
    def dfs(node):
        # Base case: if node is a leaf
        if node.left is None and node.right is None:
            return node.val
        
        # If node has only left child
        if node.left is not None and node.right is None:
            return node.val + dfs(node.left)
        
        # If node has only right child
        if node.right is not None and node.left is None:
            return node.val + dfs(node.right)
        
        # If node has both children, take the minimum path
        return node.val + min(dfs(node.left), dfs(node.right))
    
    return dfs(root)