def isSubset( a1, a2, n, m):
    s = set()
    for i in range(n) :
        s.add(a1[i])

    p = len(s)
    for i in range(m) :
        s.add(a2[i])
    if (len(s) == p) :
        return "Yes"
    return "No"
    
    
