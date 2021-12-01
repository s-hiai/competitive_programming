from collections import deque
wh_list = []
wall_list = []
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    walls = [list(map(int, input().strip().split())) for _ in range(2*h-1)]
    wh_list.append((w,h))
    wall_list.append(walls)


def bfs(wh, walls):
    w,h = wh
    next_list = [[[] for _ in range(w)] for _ in range(h)]
    for hi in range(h):
        for wi in range(w):
            if hi-1 >= 0 and walls[2*hi-1][wi] == 0:  # 上に行ける
                next_list[hi][wi].append((hi-1, wi))
            if wi+1 < w and walls[2*hi][wi] == 0: # 右に行ける
                next_list[hi][wi].append((hi, wi+1))
            if hi+1 < h and walls[2*hi+1][wi] == 0:  # 下に行ける
                next_list[hi][wi].append((hi+1, wi))
            if wi-1 >= 0 and walls[2*hi][wi-1] == 0: # 左に行ける
                next_list[hi][wi].append((hi, wi-1))
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[0][0] = 0
    que = deque([(0,0)])
    while que:
        hi, wi = que.popleft()
        cands = next_list[hi][wi]
        for ch, cw in cands:
            if dist[ch][cw] == -1:
                que.append((ch, cw))
                dist[ch][cw] = dist[hi][wi] + 1
                if ch == h-1 and cw == w-1:
                    return dist[ch][cw]
    return -1

for wh, walls in zip(wh_list, wall_list):
    print(bfs(wh, walls)+1)




