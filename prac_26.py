import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

adj_dict = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_dict[a].append(b)
    adj_dict[b].append(a)
px_list = [tuple(map(int, input().split())) for _ in range(Q)]

score_list = [0] * N
for p, x in px_list:
    score_list[p-1] += x

checked_list = []
def dfs(p, pre):
    child_list = [c for c in adj_dict[p] if c != pre]
    for child in child_list:
        score_list[child-1] += score_list[p-1]
        dfs(child, p)

dfs(1, 0)
print(*score_list)

