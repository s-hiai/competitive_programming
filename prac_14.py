from itertools import product

N, K = map(int, input().split())
a_list = list(map(int, input().split()))

init_h = a_list[0]
min_cost = float('inf')
for bits in product([0, 1], repeat=N-1):
    if sum(bits) != K-1:
        continue
    max_h = init_h
    cost = 0
    for idx, bit in enumerate(bits):
        idx = idx + 1
        if bit == 1 and a_list[idx] <= max_h:
            max_h = max_h + 1
            cost += max_h - a_list[idx]
        elif a_list[idx] > max_h:
            max_h = a_list[idx]
    if min_cost > cost:
        min_cost = cost

print(min_cost)

        
