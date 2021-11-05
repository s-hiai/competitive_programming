n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))
#S = sorted(S)

def bin_search(t):
    left = 0
    right = n
    while left < right:
        mid = int((left + right) / 2)
        if S[mid] == t:
            return mid
        elif t < S[mid]:
            right = mid
        else:
            left = mid + 1
    return -1

C = 0
for t in T:
    if bin_search(t) != -1:
        C += 1
print(C)


