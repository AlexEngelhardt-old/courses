from x2_tree_height import TreeHeight, Node


def test_tree_height():
    s = TreeHeight()
    s.n = 5
    s.parent = [4, -1, 4, 1, 1]
    s.build_tree()
    assert s.compute_height() == 3

    t = TreeHeight()
    t.n = 5
    t.parent = [-1, 0, 4, 0, 3]
    t.build_tree()
    assert t.compute_height() == 4


