S = input()
max_len = 0
for s in range(len(S)+1):
    for e in range(s, len(S)+1):
        if (e - s) > max_len and all([c in  ["A", "C", "G", "T"] for c in S[s:e]]):
            max_len = e - s
print(max_len)

