class UniorFind:
    def __init__(self):
        """记录每个节点的父节点"""
        self.father = []  # 大列表中套着小字典,键为子节点,值为父节点

    # 添加新节点到并查集,他的父节点为空
    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def merge(self, x, y):
        """
        如果发现两个节点是连通的,那么就要合并它们<祖先是相同的>,究竟把谁当做父节点是不在乎的
        Args:
            x:
            y:
        Returns:

        """
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            # 也可以写成 self.father[root_y] = root_x

    def is_connected(self, x, y):
        """
        查看两个节点是否为连通,判断父节点是否一致,当然也可以看看他们的祖先<父节点的父节点>是否一致
        Args:
            x:
            y:

        Returns:

        """
        return self.find(x) == self.find(y)

    def find(self, x):
        """
        实现原理: 不断往上遍历, 查询到根节点
        SHORTCOMING:
            if 树的深度比较大, 比如退化成链表,那么每次查询的效率比较低
            IMP 原因:并查集只是记录节点间的连通关系,而节点相互连通只需要有一个相同的祖先即可
        Args:
            x:

        Returns:

        """
        root = x  # 刚开始将当前节点默认为是父节点
        while self.father[root] is not None:  # 利用只有根节点的父节点才为None
            root = self.father[root]
        return root

    def find2(self, x):
        """
        路径压缩,降低树的深度,例如固定成2
        Args:
            x:

        Returns:

        """
        root = x
        # 循环1
        while self.father[root] is not None:  # 不断往上遍历,找到根节点
            root = self.father[root]
        # 路径压缩
        while x != root:  # 当前节点不是根节点
            original_father = self.father[x]  # x的父节点赋值给original_father
            self.father[x] = root  # 将x的父节点变成经过循环1查询到的根节点
            x = original_father  # 将当前向上遍历的节点付给x, 便于检查original_father是否为祖先
        return root
