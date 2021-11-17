def combinations(lst, n):
     
    if n == 0:
        return [[]]
     
    l =[]
    for i in range(0, len(lst)):
         
        m = lst[i]
        remLst = lst[i + 1:]
         
        for p in combinations(remLst, n-1):
            l.append([m]+p)
             
    return l