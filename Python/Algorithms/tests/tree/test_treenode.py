from algo.tree.treenode import TreeNode


def test_TreeNode():
    lst = [1, 2, None, 3]   
    expected = TreeNode(1, TreeNode(2,TreeNode(3)))
    got = TreeNode.arr_to_tree(lst)

    assert TreeNode.is_equal(expected, got)


def test_TreeNode_is_equal():
    """
    We will test if is_equal works as intented
    """

    assert not TreeNode.is_equal(None, TreeNode())

    assert TreeNode.is_equal(None, None)

    assert TreeNode.is_equal(TreeNode(1,TreeNode(2,None,TreeNode(4)), TreeNode(5)), 
                             TreeNode(1,TreeNode(2,None,TreeNode(4)), TreeNode(5)))

