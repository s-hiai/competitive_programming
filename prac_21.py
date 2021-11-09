N = int(input())
hs_list = [tuple(map(int, input().split())) for _ in range(N)]

def check_mid(x):
    th_list = [(x-h) // s for h, s in hs_list]
    th_list.sort()
    return all([th_list[i] >= i for i in range(N)])
        

left = min([h for h, _ in hs_list])
right = max([h+s*(N-1) for h, s in hs_list])
while right - left > 1:
    mid = (left + right) // 2
    if check_mid(mid):
        right = mid
    else:
        left = mid
    
print(right)

