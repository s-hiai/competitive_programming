n = int(input())
rc_list = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for l in range(2, n+1):
    for i in range(n+1-l):
        j = i+l
        min_cnt = float("inf")
        for k in range(i+1, j):
            cnt = dp[i][k] + dp[k][j] + rc_list[i][0]*rc_list[k-1][1]*rc_list[j-1][1]
            if min_cnt > cnt:
                min_cnt = cnt
        dp[i][j] = min_cnt
print(dp[0][-1])

