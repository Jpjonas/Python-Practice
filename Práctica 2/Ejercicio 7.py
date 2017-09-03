def numTriangulares(n):
    t=0
    for x in range(1,n+1):
        t=t+x
        print(x," - ",t)


def numTriangulares2(n):
    for x in range (1,n+1):
        print(x," - ",int(x*(x+1)/2))

numTriangulares(10)
numTriangulares2(10)
