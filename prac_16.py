from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

perm = tuple(permutations(range(1, N+1)))
a = perm.index(P)
b = perm.index(Q)

print(abs(a-b))


