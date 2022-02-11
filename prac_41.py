# day D T
# clothes N (A B C)
# max(sum(|ci - ci+1|))

D, N = list(map(int, input().split()))
t_list = [int(input()) for _ in range(D)]
abc_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(D)]
# 初期化
t = t_list[0]
for i in range(N):
    a, b, _ = abc_list[i]
    if not a <= t <= b:
        dp[0][i] = -1

for i in range(1, D):
    t = t_list[i]
    for j in range(N): # i+1のNパターン
        ai1, bi1, ci1 = abc_list[j]
        if not ai1 <= t <= bi1:
            dp[i][j] = -1
            continue
        diff_list = []
        for k in range(N):#iのNパターン
            if dp[i-1][k] == -1:
                continue
            ci = abc_list[k][2]
            diff_list.append(dp[i-1][k] + abs(ci1 - ci))
        dp[i][j] = max(diff_list)
print(max(dp[-1]))





