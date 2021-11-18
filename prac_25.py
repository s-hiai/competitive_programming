import sys
import itertools
sys.setrecursionlimit(10**7) 

whm_list = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(h)]
    whm_list.append((w, h, mat))

def dfs(h, w, mat):
    for dh, dw in itertools.product([-1, 0, 1], repeat=2):
        if dh == dw == 0:
            continue
        if h + dh < 0 or h + dh >= len(mat) or w + dw < 0 or w + dw >= len(mat[0]):
            continue
        if mat[h+dh][w+dw] == 1:
            mat[h+dh][w+dw] = 2
            dfs(h+dh, w+dw, mat)

def count_island(w, h, mat):
    count = 0
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                dfs(i, j, mat)
                count += 1
    return count

for w, h, mat in whm_list:
    print(count_island(w, h, mat))


