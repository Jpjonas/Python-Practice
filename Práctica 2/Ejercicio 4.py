def main():
    m=int(input("Ingrese la cantidad de factoriales: "))
    for x in range(0,m):
        n=int(input("Ingresse un valor para el calculo factorial: "))
        t=1
        for y in range(1,n+1):
            t=t*y
        print(t)

main()
