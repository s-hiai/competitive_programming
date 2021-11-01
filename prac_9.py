m = int(input())
t_xy_list = list(tuple(map(int, input().split())) for _ in range(m))

n = int(input())
xy_set = set(tuple(map(int, input().split())) for _ in range(n))

btx, bty = t_xy_list[0]
d_t_xy_list = [(btx - x, bty - y) for x, y in t_xy_list[1:]]

for bx, by in xy_set:
    for dtx, dty in d_t_xy_list:
        if (bx - dtx, by - dty) not in xy_set:
            break
    else:
        print(bx - btx, by - bty)
        exit()



