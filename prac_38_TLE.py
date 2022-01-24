N = int(input())
s_list = [input() for _ in range(2*N)]

# TLE
def lcs(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[-1][-1]


for n in range(0, N*2, 2):
    s1 = s_list[n]
    s2 = s_list[n+1]
    print(lcs(s1, s2))



