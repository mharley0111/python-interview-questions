class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def searchBSTRecursive(root: TreeNode, val: int) -> TreeNode:
	if root is None or val == root.val:
		return root
	
	return searchBSTRecursive(root.left, val) if val < root.val else searchBSTRecursive(root.right, val)

def searchBSTIterative(root: TreeNode, val: int) -> TreeNode:
	while root is not None or val != root.val:
		root = root.left if val < root.val else root.right

	return root