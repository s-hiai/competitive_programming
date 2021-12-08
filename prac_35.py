N, W = map(int, input().split())
vw_list = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    vi, wi = vw_list[i]
    for w in range(W+1):
        if w - wi >= 0:
            dp[i+1][w] = max(dp[i][w-wi]+vi, dp[i][w])
        else:
            dp[i+1][w] = dp[i][w]
print(dp[N][W])


