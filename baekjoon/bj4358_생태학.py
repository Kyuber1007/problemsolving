import sys
from collections import Counter
count = 0

spices = []
for line in sys.stdin:
    if line == '\n':
        break
    else:
        count += 1
        spices.append(line.strip())
spices.sort()

spices_dict = {}
spices_dict = Counter(spices)

for spice in spices_dict.keys():
    print(spice, f'{spices_dict.get(spice)/count * 100:.4f}')