m = int(input())
n = int(input())
mp = [tuple(map(int, input().split())) for _ in range(n)]


def get_next(i, j, checked_list):
    next_list = []
    for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0<= nj < m:
            if mp[ni][nj] == 1 and (ni, nj) not in checked_list:
                next_list.append((ni, nj))
    return next_list


def dfs(i, j, checked_list):
    next_list = get_next(i, j, checked_list)
    if next_list == []:
        return 1
    max_depth = -1
    for ni, nj in next_list:
        depth = dfs(ni, nj, checked_list + [(i, j)])
        if max_depth < depth:
            max_depth = depth
    return max_depth + 1


max_res = -1
for i in range(n):
    for j in range(m):
        if mp[i][j] == 1:
            res = dfs(i, j, [])
            if max_res < res:
                max_res = res
print(max_res)



