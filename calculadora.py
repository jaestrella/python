def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b != 0:
        return a/b
    else:
        return "No se puede dividir por 0"

print("BIENVENIDO A LA CALCULADORA DE PYTHON")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
opcion=int(input("Elige una opcion: "))


while opcion<1 or opcion >4:
    print("Opción no válida")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    opcion=int(input("Elige una opcion: "))

n1=float(input("Introduce el primer numero:"))
n2=float(input("Introduce el segundo numero:"))

if opcion==1:
    print("El resultado de la suma es:",sumar(n1,n2))
elif opcion==2:
    print("El resultado de la resta es:",restar(n1,n2))
elif opcion==3:
    print("El resultado de la multiplicacion es:",multiplicar(n1,n2))
elif opcion==4:
    print("El resultado de la division es:",dividir(n1,n2))
    