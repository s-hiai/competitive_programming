import bisect

N = int(input())
A_list = sorted(list(map(int, input().split())))
B_list = sorted(list(map(int, input().split())))
C_list = sorted(list(map(int, input().split())))

res = 0
for b in B_list:
    a_num = bisect.bisect_left(A_list, b)
    c_idx = bisect.bisect(C_list, b)
    c_num = N - c_idx
    res += a_num * c_num
print(res)
