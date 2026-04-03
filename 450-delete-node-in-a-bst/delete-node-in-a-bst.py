class Solution(object):
    def deleteNode(self, root, key):
        # если дерево пустое
        if not root:
            return None
        
        # ищем нужный узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # нашли узел
            
            # если нет левого ребенка
            if not root.left:
                return root.right
            
            # если нет правого ребенка
            if not root.right:
                return root.left
            
            # если есть оба ребенка ищем минимум справа
            temp = root.right
            while temp.left:
                temp = temp.left
            
            # заменяем значение
            root.val = temp.val
            
            # удаляем этот минимум
            root.right = self.deleteNode(root.right, temp.val)
        
        return root