n, m  = map(int, input().split())
c_list = list(map(int, input().split()))
dp = [[i for i in range(n+1)] for _ in range(m)]
for i in range(m-1):
    c = c_list[i+1]
    for j in range(n+1):
        if j - c >= 0:
            dp[i+1][j] = min(dp[i][j-c]+1, dp[i][j], dp[i+1][j-c]+1)
        else:
            dp[i+1][j] = dp[i][j]
print(dp[m-1][n])

