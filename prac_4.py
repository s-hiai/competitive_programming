N, M = map(int, input().split())
A_list = [list(map(int, input().split())) for _ in range(N)]

max_score = 0
for m1 in range(M):
    for m2 in range(m1+1, M):
        score = 0
        for n in range(N):
            score += max(A_list[n][m1], A_list[n][m2])
        if score > max_score:
            max_score = score

print(max_score)

