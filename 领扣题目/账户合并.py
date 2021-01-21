from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # self.parent 是n对应的索引下标(某个邮箱所属的联系人)

    def find(self, p):
        """
        疑问: 两个while 语句用来干嘛
        Args:
            p:

        Returns:

        """
        root = p
        while root != self.parent[root]:
            root = self.parent[root]

        while p != self.parent[p]:
            tmp = self.parent[p]
            self.parent[p] = root
            p = tmp

        return root

    def union(self, p, q):
        """
        实现:看看p_id 和q_id 是否为一致
        疑问:如何使用self.find()发现p q 是否一致,为啥0和2 是同一个
        Args:
            p:
            q:

        Returns:

        """
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        self.parent[p_id] = q_id


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """

        """
        size = len(accounts)
        if size == 0:
            return []
        res = []
        uf = UnionFind(size)
        # 邮箱 -> 用户编号
        email2id = {}
        for i in range(size):
            account = accounts[i]
            cur_size = len(account)
            for j in range(1, cur_size):
                email = account[j]
                personId = email2id.get(email, None)  # 查看email 是否存在于当前的email2id(数据都是每个邮箱对应的联系人下标)中
                if personId is None:
                    email2id[email] = i
                else:  # 存在该personId,看看如何将两个id 整合
                    uf.union(i, personId)  # i为用户编号,personId为某一个邮箱已经存在于email2id中
        # 用户编号 -> 邮箱
        id2email = {}
        for email, personId in email2id.items():
            rootId = uf.find(personId)
            rootEmailList = id2email.get(rootId, None)
            if not rootEmailList:
                tmp = []
                tmp.append(email)
                id2email[rootId] = tmp
            else:
                id2email[rootId].append(email)
        for personId, emailList in id2email.items():
            cur_acc = []
            cur_acc.append(accounts[personId][0])
            emailList.sort()
            cur_acc.extend(emailList)
            res.append(cur_acc)
        print(res)
        return res
if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

    Solution().accountsMerge(accounts)