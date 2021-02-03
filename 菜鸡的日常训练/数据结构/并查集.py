class UniorFind:
    def __init__(self):
        """记录每个节点的父节点"""
        self.father = []

    # 添加新节点到并查集,他的父节点为空
    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def merge(self, x, y, value):
        """
        如果发现两个节点是连通的,那么就要合并它们<祖先是相同的>,究竟把谁当做父节点是不在乎的
        Args:
            x:
            y:
            value:

        Returns:

        """
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

    def is_connected(self, x, y):
        """
        查看两个节点是否为连通,判断父节点是否一致,当然也可以看看他们的祖先是否一致
        Args:
            x:
            y:

        Returns:

        """
        return self.find(x) == self.find(y)

    def find(self, x):
        """
        if 节点的父节点不为空,那就不断迭代
        SHORTCOMING:
            if 树的深度比较大, 比如退化成链表,那么每次查询的效率比较低, 可以考虑做一个路径压缩<递归or 迭代 are both ok>,把树的深度固定为2
            原因:并查集只是记录节点间的连通关系,而节点相互连通只需要有一个相同的祖先即可
        Args:
            x:

        Returns:

        """
        root = x  # 刚开始将当前节点默认为是父节点
        while self.father[root] is not None:
            root = self.father[root]
        return root

    def find2(self, x):
        """
        路径压缩
        Args:
            x:

        Returns:

        """
        root = x
        # 循环1
        while self.father[root] is not None:
            root = self.father[root]
        # 路径压缩
        while x != root:
            original_father = self.father[x]  # x的直接父节点赋值给original_father
            self.father[x] = root  # 将x的直接父节点变成经过循环1查询到父节点
            x = original_father # 将当前向上遍历的节点付给x, 便于检查original_father是否为祖先
