arr = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

table = list(map(list, zip(*arr[::-1])))
print(table)

from collections import defaultdict
asdf = defaultdict(int)
asdf['asdf'] += 1
print(asdf)