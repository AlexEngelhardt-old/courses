from x1_tree_orders import TreeOrders

T = TreeOrders()
T.key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
T.left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
T.right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]

print(" ".join(str(x) for x in T.inOrder()))
print(" ".join(str(x) for x in T.preOrder()))
print(" ".join(str(x) for x in T.postOrder()))
