def sumar():
    a=int(input("Introduce el primer numero:"))
    b=int(input("Introduce el segundo numero:"))
    resultado=a+b
    return resultado

print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
opcion=int(input("Elige una opcion: "))
if opcion==1:
    print("El resultado de la suma es:",sumar())
else:
    print("Opción no válida")
