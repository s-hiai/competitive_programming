from itertools import product
import numpy as np

R, C = map(int, input().split())
a_list = [tuple(map(int, input().split())) for _ in range(R)]
na_list = np.array(a_list)
res = -1
for bits in product([0, 1], repeat=R):
    temp_na_list = []
    for idx, bit in enumerate(bits):
        if bit == 1:
            temp_na_list.append(np.where(na_list[idx] == 1, 0, 1))
        else:
            temp_na_list.append(na_list[idx])
    temp_na_list = np.array(temp_na_list)
    cand = 0
    for na in np.count_nonzero(temp_na_list == 0, axis=0):
        cand += max(na, R-na)
    res = max(res, cand)
print(res)
