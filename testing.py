# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to perform in-order traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

# Function to perform in-order traversal with tree-like printing
def inorder_traversal_with_tree_structure(root, depth=0, prefix="Root: "):
    if root:
        print(" " * depth * 4 + prefix + str(root.val))
        if root.left or root.right:
            print(" " * (depth + 1) * 4 + "├── Left:")
            inorder_traversal_with_tree_structure(root.left, depth + 1, "│    " + prefix)
            print(" " * (depth + 1) * 4 + "└── Right:")
            inorder_traversal_with_tree_structure(root.right, depth + 1, "     " + prefix)

def insert(root, val):

    if root is None:
        root = TreeNode(val, None, None)
    elif root.val < val:
        root.right = insert(root.right, val)
    elif root.val > val:
        root.left = insert(root.left, val)
    return root



def my_f(root):

    if not root:
        return 0
    
    return my_f(root.left) + my_f(root.right) + 1
        

def sumNumbers(root):
        def traverse(node, path_sum):
            if not node:
                return 0
            
            # Update the path sum by adding the current node's value
            path_sum = path_sum * 10 + node.val
            
            # If it's a leaf node, return the path sum
            if not node.left and not node.right:
                return path_sum
            
            # Otherwise, recursively traverse left and right subtrees
            return traverse(node.left, path_sum) + traverse(node.right, path_sum)
        
        # Start traversal from the root with initial path sum of 0
        return traverse(root, 0)


def minDepth(root):
    if root is None:
        return 0 

    min_depth = [float('inf')]
    dfs(root, 0, min_depth)

    return min_depth[0]

def dfs( node, cur_depth, min_depth):
    
    if node is None:
        return 

    if not node.right and not node.left:
        min_depth[0] = min(min_depth[0], cur_depth + 1)

    dfs(node.left, cur_depth + 1,min_depth)
    dfs(node.right, cur_depth + 1, min_depth)

# Test your functions
if __name__ == "__main__":
    # Create a binary search tree
    root = None
    values = [5, 3, 8, 2, 4, 7, 9]
    for value in values:
        root = insert(root, value)

    # Print the tree structure using in-order traversal
    print("In-order traversal with tree structure:")
    inorder_traversal_with_tree_structure(root)

    s = minDepth(root)
    print(s)




# class Solution(object):
#     def findkdivsmallest(self, root, k):
        
#         min_k = [float('inf')]

#         self.dfs(root, k, min_k)
#         return min_k[0]

#     def dfs(self, node, k, min_k):
#         if node is None:
#             return 

#         if node.val % k == 0:
#             min_k[0] = min(min_k[0], node.val)

#         self.dfs(node.left, k, min_k)
#         self.dfs(node.right, k, min_k)


# finding the k smallest in the tree, since we know in a bst 
# the left sub tree has the smallest node values thus
# we must serach it first
# class Solution(object):
#     def kthSmallest(self, root, k):
#         min_k = [float('inf')]
#         count = [0]
#         self.dfs(root, k, min_k, count)
#         return min_k[0]

#     def dfs(self, node, k, min_k, count):
#         if node is None:
#             return 

#         self.dfs(node.left, k, min_k, count)

#         count[0] += 1
#         if count[0] == k:
#             min_k[0] = node.val
#             return

#         if min_k[0] > node.val:  
#             min_k[0] = node.val

#         self.dfs(node.right, k, min_k, count)
        