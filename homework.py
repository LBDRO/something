from math import sqrt

def search(a):
    exitable = False
    container = {}
    for j in a:
        container[j] = True
    for m in range(0, len(a)):
        for n in range(m, len(a)):
            i = sqrt(a[m]**2+a[n]**2)
            if i in container:
                print "("+str(a[m])+", "+str(a[n])+", "+str(i)+")"
                exitable = True
    return exitable
