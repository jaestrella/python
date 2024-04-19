#solicitamos la edad
edad=int (input("Ingrese su edad: "))

#realizamos la calculadora

if edad>=18:
    nombre=input("Introduce tu nombre: ")
    altura=float(input("Introduce tu altura m: "))
    peso=float(input("Introduce tu peso kg: "))
    imc=round(peso/(altura**2),2)
    print(nombre, "tu imc es de: ",imc)

    if imc<=15.99:
        print("Delgadez severa")
    elif 16.0<= imc <=16.99:
        print("Delgadez moderada")
    elif 17.0<= imc <=18.49:
        print("Delgadez leve")
    elif 18.50<= imc <=24.99:
        print("Normal")
    elif 25.0<= imc <=29.99:
        print("Sobrepeso")
    elif 30.0<= imc <=34.99:
        print("Obesidad leve")  
    elif 35.0<= imc <=39.0:
        print("Obesidad")
    elif imc >=40.0:
        print("Obesidad morbida")
else:
    print("Usted es menor de edad.")