N = int(input())
S = input()

res_list = []
for i in range(10):
    i_p  = S.find(str(i))
    if i_p == -1:
        continue
    S_i = S[i_p+1:]
    for j in range(10):
        j_p  = S_i.find(str(j))
        if j_p == -1:
            continue
        S_j = S_i[j_p+1:]
        for k in range(10):
            if S_j.find(str(k)) != -1:
                res_list.append((i, j, k))
print(len(res_list))
            
