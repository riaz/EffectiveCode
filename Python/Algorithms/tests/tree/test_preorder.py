from algo.tree.treenode import TreeNode
from algo.tree.preorder import preorder_traversal

def test_preorder_traversal():
    tree = TreeNode(10)
    assert [10] == preorder_traversal(tree)

    tree = TreeNode(10, TreeNode(20), TreeNode(30))
    assert [10,20,30] == preorder_traversal(tree)

    left = TreeNode(10, TreeNode(20), TreeNode(30))
    right = TreeNode(10, TreeNode(20), TreeNode(30))
    tree = TreeNode(10, left, right)

    assert [10,10,20,30,10,20,30] == preorder_traversal(tree)
    