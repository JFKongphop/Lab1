usd = 30.85 
def check (n):
    if(n > 0):
        bth =  usd * n
        print(bth)

        sb = str(bth)
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

    else:
        print("invalid")

check(5)

