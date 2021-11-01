from itertools import product
from itertools import combinations

N, M = map(int, input().split())
xy_set = set(tuple(map(int, input().split())) for _ in range(M))

max_ptnum = -1
for bits in product([0, 1], repeat=N):
    cand = [idx+1 for idx, b in enumerate(bits) if b == 1]
    for cp in combinations(cand, 2):
        if cp not in xy_set:
            break
    else:
        max_ptnum = max(max_ptnum, len(cand))

print(max_ptnum)

