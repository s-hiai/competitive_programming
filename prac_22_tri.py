
P = float(input())

t = lambda x:x + P * 2 ** -(x/1.5) # ここ割り算したらオーバーフローする

left = 0
right = P+1
while left + 10 ** -8 < right:
    c1 = left + (right - left) / 3
    c2 = right - (right - left) / 3
    if t(c1) < t(c2):
        right = c2
    else:
        left = c1

print(t(left))

