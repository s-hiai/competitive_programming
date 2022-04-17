N = int(input())
a_list = [int(input()) for _ in range(N)]
ad_list = a_list + a_list

def p(dp):
    for r in dp:
        print(r)
    print("-"*30)

dp = [[0 for _ in range(2*N+1)] for _ in range(2*N+1)]

for span in range(1, N+2):
    for i in range(N):
        j = i + span
        print(span, i, j)
        is_joi = not bool((N - span) % 2)
        if is_joi:
            dp[i][j] = max(dp[i+1][j]+ad_list[i],
                           dp[i][j-1]+ad_list[j-1])
        else:
            if ad_list[i] > ad_list[j-1]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i][j-1]
    p(dp)
    
#print([dp[i][N+i] for i in range(N)])
print(max([dp[i][N+i] for i in range(N)]))
