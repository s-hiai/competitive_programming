from collections import deque
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

b_num = 0
for line in field:
    b_num += line.count('#')

def bfs():
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    que = deque([(0,0)])
    dist[0][0] = 1
    while que:
        h, w = que.popleft()
        if h == H-1 and w == W-1:
            return dist[h][w]
        if h - 1 >= 0 and dist[h-1][w] == -1 and field[h-1][w] == '.':
            que.append((h-1, w))
            dist[h-1][w] = dist[h][w] + 1
        if h + 1 < H and dist[h+1][w] == -1 and field[h+1][w] == '.':
            que.append((h+1, w))
            dist[h+1][w] = dist[h][w] + 1
        if w - 1 >= 0 and dist[h][w-1] == -1 and field[h][w-1] == '.':
            que.append((h, w-1))
            dist[h][w-1] = dist[h][w] + 1
        if w + 1 < W and dist[h][w+1] == -1 and field[h][w+1] == '.':
            que.append((h, w+1))
            dist[h][w+1] = dist[h][w] + 1
    return -1

path_num = bfs()
if path_num == -1:
    print(-1)
else:
    print(W*H -b_num - path_num)

