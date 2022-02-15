N = int(input())
s_mat = [list(input()) for _ in range(5)]
s_id = {"R":0, "B":1, "W":2, "#":3}

dp = [[[float("inf") for _ in range(3)] for _ in range(3)] for _ in range(N)]

for i in range(3):
    paint_count = 0
    for k in range(5):
        if s_id[s_mat[k][0]] != i:
            paint_count += 1
    for j in range(3):
        dp[0][i][j] = paint_count
#print(dp)

for n in range(1, N):
    for s in range(3):
        for ps in range(3):
            if s == ps:
                continue
            paint_count = 0
            for k in range(5):
                if s_id[s_mat[k][n]] != s:
                    paint_count += 1
            dp[n][s][ps] = min(dp[n-1][ps]) + paint_count
#print(dp)
res = float("inf")
for i in range(3):
    for j in range(3):
        res = min(res, dp[-1][i][j])
print(res)
