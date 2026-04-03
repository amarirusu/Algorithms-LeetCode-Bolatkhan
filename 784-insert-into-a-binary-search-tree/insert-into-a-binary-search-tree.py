class Solution(object):
    def insertIntoBST(self, root, val):
        # если дерево пустое создаем новый узел
        if not root:
            return TreeNode(val)
        
        # если значение меньше идем влево
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            # если больше или равно идем вправо
            root.right = self.insertIntoBST(root.right, val)
        
        # возвращаем корень
        return root