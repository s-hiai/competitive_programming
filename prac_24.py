n = int(input())
ukv_list = [list(map(int, input().split())) for _ in range(n)]
round_list = []
def dfs(u):
    if u in round_list:
        return
    round_list.append(u)
    v_list = ukv_list[u-1][2:]
    for v in v_list:
        dfs(v)
    round_list.append(u)

for u in range(n):
    if u+1 not in round_list:
        dfs(u+1)

for u in range(n):
    print(u+1, " ".join([str(i+1) for i, v in enumerate(round_list) if v == u+1]))

