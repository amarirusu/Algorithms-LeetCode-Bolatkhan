class Solution:
    def inorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)   # идем влево
            result.append(node.val)  # добавляем корень
            dfs(node.right)  # идем вправо

        dfs(root)
        return result