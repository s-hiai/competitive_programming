import bisect

N, M = map(int, input().split())
P_list = [int(input()) for _ in range(N)] + [0]
q_list = []
for p1 in P_list:
    for p2 in P_list:
        q_list.append(p1 + p2)
q_list.sort()

max_score = -1
for q in q_list:
    if M-q < 0:
        continue
    max_idx = bisect.bisect(q_list, M-q)-1
    score = q+q_list[max_idx]
    if score > max_score:
        max_score = score
print(max_score)





