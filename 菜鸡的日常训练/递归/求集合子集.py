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
