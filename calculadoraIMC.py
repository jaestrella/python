name=input("Introduzca su nombre: ")
high=float(input("Introduzca su altura: "))
weight=float(input("Introduzca su peso: "))
sex=input("Introduzca su sexo: ")
imc=weight/(high*high)
print()
print(name, "con altura", high, ", peso", weight, "y",sex, "su indice de masa corporal es:", round(imc,2))