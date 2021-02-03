from typing import List


class UnionFind:
    def __init__(self):
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0

    def find(self, x):
        root = x

        while self.father[root] is not None:
            root = self.father[root]

        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(M)):
            uf.add(i)  # 为啥要添加i,每个i 相当于某个城市<不管三七二十一, 先添加, 然后下面通过判断进一步筛选>
            for j in range(i):  # 只遍历i城市之前的城市, 缩小查询次数
                if M[i][j]:  # 先查看是否两个城市连通
                    uf.merge(i, j)  # 如果两个城市相互连通,那么对应坐标也应该同时为1

        return uf.num_of_sets


if __name__ == '__main__':
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    res = Solution().findCircleNum(isConnected)
    print(res)
