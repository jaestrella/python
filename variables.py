# variables

my_string_varibale="Mi nombre es jose"
print(my_string_varibale)

my_int_variable=5
print(my_int_variable)

my_boolean_variable=True
print(type(my_boolean_variable))

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# concatenacion de varibles

print(my_string_varibale,my_int_variable,my_boolean_variable)

print("Mi edad es de",my_int_variable,"años")

# vamos a ver la funcion len que cuenta caracteres

print(len(my_string_varibale))

# variables de una linea

name,surname,age=("jose","estrella",80)
print("me llamo",name,surname,"y tengo",age)

name1, email, password=("paco","jimenez@gmail.com","123456789")
print("Hola " + name1,",", "¿tu email", email, "y contraseña", password,"son correctos?")

# inputs

name2=input("Introduce tu nombre:")
age2=input("Introduce tu edad:")
