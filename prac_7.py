from itertools import combinations

n = int(input())
xy_list = [tuple(map(int, input().split())) for _ in range(n)]
xy_set = set(xy_list)
res = 0
for xy1, xy2 in combinations(xy_set, 2):
    x1, y1 = xy1
    x2, y2 = xy2
    x3 = x1 - (y2 - y1)
    y3 = y1 + (x2 - x1)
    x4 = x2 - (y2 - y1)
    y4 = y2 + (x2 - x1)
    if (x3, y3) in xy_set and (x4, y4) in xy_set:
        res = max(res, (x1 - x2) ** 2 + (y1 - y2) ** 2)
print(res)
