# funciones sin args y sin retorno

def saludar():
    print("hola")

saludar()

# funciones con args pero sin retorno

def sumar(a,b):
    resultado=a+b
    print("El resultado es: ", resultado)
sumar(1,1)

# funciones con argumentos y retorno

def multiplicar(a,b):
    return a*b
resultado=multiplicar(5,5)
print("El resultado es: ",resultado)

# funciones con args predeterminados

def saludar(nombre="Juan"):
    print("Hola", nombre)
saludar()
saludar("pepe")