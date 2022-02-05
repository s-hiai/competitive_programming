N, K = map(int, input().split())
ab_list = [map(int, input().split()) for _ in range(K)]
ab_dict = {a-1:b-1 for a, b in ab_list}

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N)]

#print(sorted(ab_dict.items(), key=lambda x:x[0]))
if 0 in ab_dict and 1 in ab_dict:
    dp[1][ab_dict[1]][ab_dict[0]] = 1
elif 0 in ab_dict:
    for i in range(3):
        dp[1][i][ab_dict[0]] = 1
elif 1 in ab_dict:
    for i in range(3):
        dp[1][ab_dict[1]][i] = 1
else:
    for i in range(3):
        for j in range(3):
            dp[1][i][j] = 1
#print(dp)

for i in range(2, N):
    for a in range(3):
        for b in range(3):
            for c in range(3):
                if i != 1 and a == b == c:
                    continue
                if i in ab_dict and a != ab_dict[i]:
                    continue
                dp[i][a][b] += dp[i-1][b][c]
                dp[i][a][b] %= 10000
"""for i, d_dp in enumerate(dp):
    if i in ab_dict:
        print(i, d_dp, ab_dict[i])
    else:
        print(i, d_dp, -1)"""
res = 0
for i in range(3):
    res += sum(dp[-1][i])
print(res % 10000)
