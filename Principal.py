from Funciones import *

print("Division por restas sucesivas. ")

dividendo_1 = int(input("Introduce dividendo"))
divisor1 = int(input("Introduce divisor"))
if divisor1 == 0:
    print("Error! Division entre cero")
elif dividendo_1 < divisor1:
    print("Respuesta = 0")
elif dividendo_1 > divisor1:
    print("Respuesta =", Division_Resta(dividendo_1, divisor1))



print("\nSuma de cada digito ingresado. ")

sumatoria = 0
print ("Usa 0 para terminar")
num = int(input("Numero a procesar"))
while num != 0:
    print("Suma: ", SumaDigitos(num))
    sumatoria += num
    print("Usa 0 para terminar")
    num = int(input("Numero a procedar"))
print("Sumatoria:", sumatoria)
print("digitos:", SumaDigitos(sumatoria))




print("\nMetodo euler ")

lim = int(input("Introduce limite "))
print("Aproximacion pi", MetodoEuler(lim)*2)




print("\nNumero primo o compuesto ")

numero = int(input("\nIngrese numero: "))
if primo_compuesto(numero):
    print("Es primo.")
else:
    print("Es compuesto.")



print("\nFactorización prima de un valor factorial")

numero = int(input("Ingrese valor para calcular su factorización prima: "))
if primo_compuesto(Factorial(numero)):
     print(f"{Factorial(numero)}!  Es primo.")
else:
     print(f"{Factorial(numero)}!  Es compuesto.")
