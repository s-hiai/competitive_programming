from itertools import permutations

N = int(input())
xy_list = [tuple(map(int, input().split())) for _ in range(N)]

route_list = list(permutations(range(len(xy_list))))
sum_dist = 0
for route in route_list:
    for idx in range(N-1):
        sx, sy = xy_list[route[idx]]
        ex, ey = xy_list[route[idx+1]]
        sum_dist += ((sx - ex) ** 2 + (sy - ey) ** 2) ** (1/2)
print(sum_dist / len(route_list))
