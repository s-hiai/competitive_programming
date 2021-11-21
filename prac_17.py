import itertools
k = int(input())
rc_list = [tuple(map(int, input().split())) for _ in range(k)]

perm_list = []
for c_perm in itertools.permutations(list(range(8))):
    cand = set()
    for c, r in zip(c_perm, range(8)):
        cand.add((r, c))
    perm_list.append(cand)

cand_list = []
for cand in perm_list:
    if all([rc in cand for rc in rc_list]):
        cand_list.append(cand)

# 斜めの判定
res = []
for cand in cand_list:
    for r, c in cand:
        for rsign, csign in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
            rd = r + rsign
            cd = c + csign
            while 0 <= rd <= 7 and 0 <= cd <= 7:
                if (rd, cd) in cand:
                    break
                rd += rsign
                cd += csign
            else:
                continue
            break
        else:
            continue
        break
    else:
        res = cand
        break

for i in range(8):
    print("".join(['Q' if (i, j) in res else '.' for j in range(8)]))

