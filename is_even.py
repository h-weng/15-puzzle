def is_even(p):
    sign=1
    s=0
    u=0
    while s < len(p):
        m=p[s]
        u=s+1
        l=s
        while u < len(p):
            if p[u] < m:
                m = p[u]
                l = u
            u = u + 1

        if p[s] != p[l]:
            p[s], p[l] = p[l], p[s]
            sign = 1 - sign
            print(p)
        s = s + 1
    return bool(sign)

print(is_even([0, 4, 3, 2, 1])) 
