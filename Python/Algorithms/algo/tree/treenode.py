class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right
    
    @staticmethod
    def arr_to_tree(arr: list[int]) -> "TreeNode":
        """
        This function takes in a list and converts it into a tree
        """
        def generate_tree(idx) -> "TreeNode":
            if idx >= len(arr) or not arr[idx]:
                return None
            node = TreeNode(arr[idx])
            node.left = generate_tree(2*idx+1)
            node.right = generate_tree(2*idx+2)
            return node
        return generate_tree(0)
    
    @staticmethod
    def is_equal(tree_a: "TreeNode", tree_b: "TreeNode") -> bool:
        """
        This function checks if the values in two trees are identical and returns true if they are
        """
        if not tree_a and not tree_b:
            return True
        if (tree_a and not tree_b) or (not tree_a and tree_b):
            return False
        return tree_a.val == tree_b.val and TreeNode.is_equal(tree_a.left, tree_b.left) and TreeNode.is_equal(tree_a.right, tree_b.right)
        
        
    