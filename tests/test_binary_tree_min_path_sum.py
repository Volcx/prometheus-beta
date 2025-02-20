import pytest
from src.binary_tree_min_path_sum import TreeNode, find_minimum_path_sum

def test_minimum_path_sum_single_node():
    root = TreeNode(5)
    assert find_minimum_path_sum(root) == 5

def test_minimum_path_sum_linear_tree():
    # 1
    #  \
    #   3
    #    \
    #     4
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    assert find_minimum_path_sum(root) == 8

def test_minimum_path_sum_balanced_tree():
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert find_minimum_path_sum(root) == 8  # 1 -> 3 -> 4

def test_minimum_path_sum_unbalanced_tree():
    #       10
    #      /  \
    #     2    8
    #    /      \
    #   1        3
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(3)
    assert find_minimum_path_sum(root) == 13  # 10 -> 2 -> 1

def test_empty_tree_raises_error():
    with pytest.raises(ValueError, match="Tree cannot be empty"):
        find_minimum_path_sum(None)