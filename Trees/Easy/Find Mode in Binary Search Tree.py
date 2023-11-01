class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findMode(self, root) -> list[int]:
        node_freq = {}
        def dfs(node, counter):
            if not node: return
            count = counter.get(node.val, 0)
            counter[node.val] = count + 1
            dfs(node.left, counter)
            dfs(node.right, counter)

        dfs(root, node_freq)
        max_frq = max(node_freq.values())
        return [node for node, freq in node_freq.items() if freq == max_frq]

solution = Solution()
# root = [1,null,2,2]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
result = solution.findMode(root)
print(result)
