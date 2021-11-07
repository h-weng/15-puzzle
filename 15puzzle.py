"""

    15 Puzzle Python Implementation
    ===============================

    This implementation is based on Breadth First Search and uses functional programming

    15 Puzzle:
    
        https://en.wikipedia.org/wiki/15_puzzle
        https://github.com/MilanPecov/15-Puzzle-Solvers
        https://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/15-puzzle.pdf
        https://www.whitman.edu/Documents/Academics/Mathematics/2017/Howe.pdf

    Breadth First Search:
    
        https://en.wikipedia.org/wiki/Breadth-first_search
        https://www.cs.cmu.edu/afs/cs/academic/class/15210-s15/www/lectures/bfs-notes.pdf
    
"""

puz = [[1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11, 12], [9, 13, 14, 15]] #jumbled puzzle
end = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] #puzzle solution

r = len(puz)
c = len(puz[0])

def swap(a, b, c, d, n):
    """swap positions using coordinates a,b and c,d, n is for number"""
    p = [list(r) for r in n]
    p[a][b], p[c][d] = p[c][d], p[a][b]
    return p

def getc(v, p):
    """get the coordinates of a value in a puzzle"""
    if not p:
        p = puz
    for i in range(r):
        for j in range(c):
            if p[i][j] == v:
                return i, j

def getm(n):
    """get moves"""
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
    """get inversion count"""
    icount = 0
    plist = [n for r in p for n in r if n != 0]
    for i in range(len(plist)):
        for j in range(i+1, len(plist)):
            if plist[i] > plist[j]:
                icount += 1
    return icount

def bcount(p):
    """blank space count"""
    zr, _ = getc(0, p)
    return r - zr

def even(n):
    """is inversion even"""
    return n % 2 == 0

def odd(n):
    """is inversion odd"""
    return n % 2 != 0

def solvable(p):
    """is puzzle solvable"""
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
    """breadth first search to solution""" 
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
d = [] #solution list

#find the path and solution to the puzzle
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
