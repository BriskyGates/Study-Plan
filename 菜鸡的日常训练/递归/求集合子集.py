# 方式1
def PowerSetsBinary(items):
    N = len(items)
    for i in range(2 ** N):  # enumerate the 2**N possible combinations
        combo = []
        for j in range(N):
            if (i >> j) % 2 == 1:  # jth bit of Integer i
                combo.append(items[j])  # generate all combination of N items
        yield combo


"""
[]
['a']
['b']
['a', 'b']
['c']
['a', 'c']
['b', 'c']
['a', 'b', 'c']
"""

# 方式2
"""
实现思路:
    利用递归进层
    为什么
"""


def PowerSetsRecursive(items):
    """Use recursive call to return all subsets of items, include empty set"""

    if len(items) == 0:
        # if the lsit is empty, return the empty list
        return [[]]

    subsets = []
    first_elt = items[0]  # first element
    rest_list = items[1:]

    # Strategy: Get all subsets of rest_list;
    # for each of those subsets,a full subset list will contain both the original subset
    # as well as a version of the subset that contains the first_elt(according to my a_2 思路,you will understand this)

    for partial_subset in PowerSetsRecursive(rest_list):
        subsets.append(partial_subset)
        next_subset = partial_subset[:] + [first_elt]  # next_subset depends on the return value of recursive function
        subsets.append(next_subset)
    print(subsets)
    return subsets  # 递归退层后都要  返回递归进层的subsets


# 方式3
"""
实现思路:
    将每个子集和新元素结合
"""


def PowerSetsRecursive2(items):
    # items need to depend on the former ones , then form into new results
    # the power set of the  set <集合的幂集> has one element at least
    result = [[]]
    for x in items:
        # 两个列表相加和extend同理
        result.extend([subset + [x] for subset in result])
    return result


if __name__ == '__main__':
    PowerSetsRecursive([1, 2, 3])
    # PowerSetsRecursive2([1, 2, 3])
