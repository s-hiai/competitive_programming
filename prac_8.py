N = int(input())
AB_list = [list(map(int, input().split())) for _ in range(N)]

A_list = [a for a, b in AB_list]
B_list = [b for a, b in AB_list]

sA_list = sorted(A_list)
sB_list = sorted(B_list)


if N%2 != 0:
    md = int((N-1)/2)
    st = sA_list[md]
    en = sB_list[md]
    dist = 0
    for a, b in AB_list:
        dist += abs(st - a) + abs(a - b) + abs(b - en)
    print(dist)
else:
    md1 = int(N/2)
    st = sA_list[md1]
    en = sB_list[md1]
    dist1 = 0
    for a, b in AB_list:
        dist1 += abs(st - a) + abs(a - b) + abs(b - en)

    md2 = md1 - 1
    st = sA_list[md2]
    en = sB_list[md2]
    dist2 = 0
    for a, b in AB_list:
        dist2 += abs(st - a) + abs(a - b) + abs(b - en)
        
    print(min(dist1, dist2))

    




