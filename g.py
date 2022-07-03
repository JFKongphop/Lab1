def putList():
    l = []
    for i in range(3):
        n = int(input("enter number : "))
        l.append(n)
    return(l)

def bubbleMed(n):
    k = len(n)
    for i in range(k):
        for j in range(n-i-1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    print(n)

bubbleMed(putList())
 