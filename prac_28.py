from collections import deque
n = int(input())
ukv_list = [list(map(int, input().split())) for _ in range(n)]
v_dict = {}
for ukv in ukv_list:
    u = ukv[0]
    k = ukv[1]
    v_list = ukv[2:]
    v_dict[u] = v_list

def dfs(target):
    checked_set = set()
    que = deque([(1,0)])
    while que:
        v, d = que.popleft()
        if v == target:
            return d
        checked_set.add(v)
        next_v = v_dict[v]
        que.extend([(n, d+1) for n in next_v if n not in checked_set])
    return -1

for i in range(1, n+1):
    print(i, dfs(i))

