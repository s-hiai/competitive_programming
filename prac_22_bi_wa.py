import math
from scipy import optimize

P = float(input())

t = lambda x:x + P * 2 ** -(x/1.5)
dt = lambda x:1 - (2/3) * P * 2 ** ((-2*x)/3) * math.log(2)

left = -100 # ここどうやって決めれば良いのだろう・・・
right= P + 1
tx = t(optimize.bisect(dt, left, right)) # t(x)の誤差をどうやって保証するのか
print(tx if tx >= 0 else t(0))
