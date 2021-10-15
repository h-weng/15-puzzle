puz = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [9, 13, 14, 15]]
end = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

r = len(puz)
c = len(puz[0])

def swap(a, b, c, d, n):
    p = [list(r) for r in n]
    p[a][b], p[c][d] = p[c][d], p[a][b]
    return p

def getc(v, p):
    if not p:
        p = puz
    for i in range(r):
        for j in range(c):
            if p[i][j] == v:
                return i, j

def getm(n):
    m = []
    i, j = getc(0, n)
    if i > 0:
        m.append(swap(i, j, i-1, j, n))
    if j < c-1:
        m.append(swap(i, j, i, j+1, n))
    if j > 0:
        m.append(swap(i, j, i, j-1, n))
    if i < r-1:
        m.append(swap(i, j, i+1, j, n))
    return m

def getinv(p):
    icount = 0
    plist = [n for r in p for n in r if n != 0]
    for i in range(len(plist)):
        for j in range(i+1, len(plist)):
            if plist[i] > plist[j]:
                icount += 1
    return icount

def bcount(p):
    zr, _ = getc(0, p)
    return r - zr

def even(n):
    return n % 2 == 0

def odd(n):
    return n % 2 != 0

def solvable(p):
    icount = getinv(p)
    bpos = bcount(p)

    if odd(r) and even(icount):
        return True
    elif even(r) and even(bpos) and odd(icount):
        return True
    elif even(r) and odd(bpos) and even(icount):
        return True
    else:
        return False

def bfs(p, e):
    q = [[p]]
    exp = []
    nodes = 0
    path = None
    while q:
        path = q[0]
        q.pop(0)
        enode = path[-1]
        if enode in exp:
            continue
        for m in getm(enode):
            if m in exp:
                continue
            q.append(path + [m])
        exp.append(enode)
        nodes += 1
        if enode == e:
            break
    exp = nodes
    return path

if not solvable(puz):
    print("[]")

paths = bfs(puz, end)
pu = [i for s in puz for i in s]
c = []
d = []
for p in paths:
    l = [i for s in p for i in s]
    if paths[0] == p:
        if l != pu:
            for n in range(len(l)):
                if l[n] != pu[n] and l[n] != 0:
                    d.append(l[n])
        pu = l
    else:
        if l != pu:
            for n in range(len(l)):
                if l[n] != pu[n] and l[n] != 0:
                    d.append(l[n])
        pu = l
print(d)
