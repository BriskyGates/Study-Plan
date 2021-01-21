import collections
from typing import List


class Solution:
    def build_graph(self, accounts):
        """
        建图
        """
        graph = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            # 对剩余账户做一个去重
            for email in list(set(account[2:])):
                graph[master].append(email)  # 双向图的用意
                graph[email].append(master)

        return graph

    def dfs(self, email, graph, visited, emails):
        """
        深搜遍历
        """
        # 已经访问过的就剪枝
        if email in visited:
            return

        visited.add(email)  # 添加遍历过的邮箱,因为列表时可变数据类型, 在子函数中对其的更改也能成功返回出
        emails.append(email)  # 某用户对应的邮箱列表

        # 对邻居节点继续深搜
        for neighbor in graph[email]:
            self.dfs(neighbor, graph, visited, emails)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = self.build_graph(accounts)

        res = []
        visited = set()
        for account in accounts:
            emails = []
            self.dfs(account[1], graph, visited, emails)
            if emails:
                res.append([account[0]] + sorted(emails))
        print(res)
        return res

if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

    Solution().accountsMerge(accounts)