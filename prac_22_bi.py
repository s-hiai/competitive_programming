import math
P = float(input())

t = lambda x:x + P * 2 ** -(x/1.5)
dt = lambda x:1 - (2/3) * P * 2 ** ((-2*x)/3) * math.log(2)

l = 0 # dt(x)=0となるxが0より小さくてもrは0（=l）に近付いていく
r = 10**10
while r - l > 0.000001:
    mid = (r+l) /2
    a = dt(mid)
    if a > 0:
        r = mid
    else:
        l = mid

print(t(l))
