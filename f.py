def meann(a,b,c):
    avg = (a+b+c) / 3
    return avg

def check(n):
    sb = str(n)
    ns = len(sb)
    indexNS = 0
    for i in range(ns):
        if sb[i] == ".":
            indexNS = i

    cutBefore = ""
    for i in range(ns):
        if i < indexNS:
            cutBefore += sb[i]

    cutAfter = ""
    just2 = "" 
    for i  in range(ns):
        if i>indexNS :
            cutAfter += sb[i]
    for i in range(2):
        just2 += cutAfter[i]
    real = f"{cutBefore}.{just2}"
    print(real)

check(meann(1,3,9.9))