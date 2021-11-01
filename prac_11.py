from itertools import product

N, M = map(int, input().split())
ks_list = [list(map(int, input().split())) for _ in range(M)]
p_list = list(map(int, input().split()))

res = 0
for bits in product([0, 1], repeat=N):
    for ks, p in zip(ks_list, p_list):
        k, s_list = ks[0], ks[1:]
        on_cnt = 0
        for s in s_list:
            if bits[s-1] == 1:
                on_cnt += 1
        if on_cnt % 2 != p:
            break
    else:
        res += 1

print(res)

        
