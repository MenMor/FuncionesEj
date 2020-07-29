from Funciones import *


Div1 = int(input("Introduce dividendo"))
Divisor1 = int(input("Introduce divisor"))
if Divisor1 == 0:
    print("Error! Division entre cero")
elif Div1 < Divisor1:
    print("Respuesta = 0")
elif Div1 > Divisor1:
    print("Respuesta =", Division_Resta(Div1, Divisor1))

print(" ")

sumatoria = 0
print ("Usa 0 para terminar")
num = int(input("Numero a procesar"))
while num != 0:
    print("Suma: ", SumaDigitos(num))
    sumatoria += num
    print("Usa 0 para terminar")
    num = int(input("Numero a procedar"))
print("Sumatoria:",sumatoria)
print("digitos:", SumaDigitos(sumatoria))

print(" ")

#metodo euler
lim = int(input("Introduce limite "))
print("Aproximacion pi",MetodoEuler(lim)*2)

print(" ")

# numero primo
num = int(input("Introduce un numero para verificar que sea primo"))
if Primo(num):
    print("Es primo")
else:
    print("No es primo")


