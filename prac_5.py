A, B, C, X, Y = map(int, input().split())

if X >= Y:
    c1 = Y * A + Y * B
    c2 = 2 * Y * C

    c3 = (X-Y) * A
    c4 = 2 * (X-Y) * C
    
    res = min(
        c1 + c3,
        c1 + c4,
        c2 + c3,
        c2 + c4
    )
else:
    c1 = X * A + X * B
    c2 = 2 * X * C

    c3 = (Y-X) * B
    c4 = 2 * (Y-X) * C
    
    res = min(
        c1 + c3,
        c1 + c4,
        c2 + c3,
        c2 + c4
    )
print(res)

    
