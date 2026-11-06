class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5


print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)

print(root.right.left)
print(root.left.left.left)
print(root.left.right.val)