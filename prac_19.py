d = int(input())
n = int(input())
m = int(input())
d_list = [0] + [int(input()) for _ in range(n-1)] + [d] # 店の位置
k_list = [int(input()) for _ in range(m)] # 宅配先の位置

sd_list = sorted(d_list)

def bin_search(k):
    left = 0
    right = n + 1
    while right - left > 1:
        mid = int((left + right)/2)
        if k < sd_list[mid]:
            right = mid
        else:
            left = mid
    return min(k - sd_list[left], sd_list[right] - k)

res = 0
for k in k_list:
    res += bin_search(k)
print(res)


