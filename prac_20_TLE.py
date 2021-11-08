"""
TLE解法
"""
import bisect

N = int(input())
A_list = sorted(list(map(int, input().split())))
B_list = sorted(list(map(int, input().split())))
C_list = sorted(list(map(int, input().split())))

res = 0
for a in A_list:
    b_st_idx = bisect.bisect(B_list, a)
    for b_idx in range(b_st_idx, N):
        b = B_list[b_idx]
        c_idx = bisect.bisect(C_list, b)
        c_num = N - c_idx
        res += c_num
print(res)


