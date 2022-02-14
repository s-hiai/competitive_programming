N, M = map(int, input().split(" "))

n_list = [int(input()) for _ in range(N)]
m_list = [int(input()) for _ in range(M)]

dp = [[float("inf") for _ in range(N+1)] for _ in range(M+1)]
for m in range(M+1):
    dp[m][0] = 0

for m in range(1, M+1):
    for n in range(1, N+1):
        dp[m][n] = min(dp[m-1][n], dp[m-1][n-1]+m_list[m-1]*n_list[n-1])
print(dp[-1][-1])

