from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

maze = [list(input()) for _ in range(R)]
dist = [[-1] * C for _ in range(R)]

def bfs(start, end):
    checked_set = set()
    que = deque([start])
    dist[start[0]-1][start[1]-1] = 0
    while que:
        (r, c) = que.popleft()
        if (r, c) == end:
            return dist[r-1][c-1]
        for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if maze[r+dr-1][c+dc-1] == "." and dist[r+dr-1][c+dc-1] == -1:
                dist[r+dr-1][c+dc-1] = dist[r-1][c-1]+1
                que.append((r+dr, c+dc))

print(bfs((sy, sx), (gy, gx)))
