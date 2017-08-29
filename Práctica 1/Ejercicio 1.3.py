def menu():
    print("MENU:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplica")
    print("4. Divide")
    print("5. Sair")
    m=int(input("Elija una opción: "))
    if(m>5)or(m<1):
        menu()
    else:
        if(m!=5):
            a=int(input("Informe el primer número: "))
            b=int(input("Informe el segundo número: "))
            if(m==1):
                print(suma(a,b))
                menu()
            if(m==2):
                print(resta(a,b))
                menu()
            if(m==3):
                print(multiplica(a,b))
                menu()
            if(m==4):
                print(divide(a,b))
                menu()

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    if(b!=0):
        return a/b

menu()
