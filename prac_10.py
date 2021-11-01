n = int(input())
a_list = list(map(int, input().split()))
q = int(input())
m_list = list(map(int, input().split()))
res_list = ["no"] * q
a = 0
for i in range(2 ** n):
    s = 0
    for beam, flag in enumerate(bin(a)[2:].zfill(n)):
        if flag == '1':
            s += int(a_list[beam])
    for idx, m in enumerate(m_list):
        if s == m:
            res_list[idx] = "yes"
    a += 1
print("\n".join(res_list))


