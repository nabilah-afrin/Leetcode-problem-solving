# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# leetcode daily challenge - day 04
# 02/11/2023

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter = 0

        def post_order(root):
            #global counter
            nonlocal counter #unboundlocalerror
            if root is None:
                return (0, 0)  # sum and count

            # return sum and count for left and right child
            left_sum, left_count = post_order(root.left)
            right_sum, right_count = post_order(root.right)

            # find the total sum of the current node
            node_sum = left_sum + right_sum + root.val
            node_count = left_count + right_count + 1

            avg = node_sum // node_count  

            if avg == root.val:
                counter += 1
            return node_sum, node_count
        
        post_order(root)
        return counter #return the count of nodes
