from collections import deque
H, W, N = map(int, input().split())
field = [list(input()) for _ in range(H)]

def bfs(start, goal):
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    que = deque([start])
    dist[start[0]][start[1]] = 0
    while que:
        nh, nw = que.popleft()
        if (nh, nw) == goal:
            return dist[nh][nw]
        for dh, dw in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            if 0 <= nh + dh < H and 0 <= nw + dw < W:
                cand = field[nh + dh][nw + dw]
                if cand != 'X' and dist[nh + dh][nw + dw] == -1:
                    que.append((nh+dh, nw+dw))
                    dist[nh+dh][nw+dw] = dist[nh][nw] + 1
    return False

target_list = ['S'] + [str(i+1) for i in range(N)]
target_cell_list = []
for target in target_list:
    for i in range(H):
        for j in range(W):
            if target == field[i][j]:
                target_cell_list.append((i, j))

dist = 0
for i in range(N):
    start = target_cell_list[i]
    goal = target_cell_list[i+1]
    dist += bfs(start, goal)

print(dist)
