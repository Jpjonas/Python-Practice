def main(c,x,n):
    t=1
    for y in range(0,n):
        t=t*(1+(x/100))
    print(c*t)

main(10,90,10)
