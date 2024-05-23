from algo.tree import TreeNode
from typing import Optional, List

def preorder_traversal(root: Optional[TreeNode]) -> List[TreeNode]:
    return [root.val] +  preorder_traversal(root.left) + preorder_traversal(root.right) if root else []