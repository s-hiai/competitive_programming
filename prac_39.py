N = int(input())
n_list = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(N-1)]
dp[0][n_list[0]] = 1

for i in range(N-2):
    for j in range(21):
        if j-n_list[i+1] >= 0:
            dp[i+1][j] += dp[i][j-n_list[i+1]]
        if j+n_list[i+1] <= 20:
            dp[i+1][j] += dp[i][j+n_list[i+1]]
print(dp[N-2][n_list[-1]])

