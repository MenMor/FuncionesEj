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

numero = int(input("\nIngrese número: "))
if primo_compuesto(numero):
    print("Es primo.")
else:
    print("Es compuesto.")

print("\nNumero primo o compuesto y sus valores divisibles:")

num = int(input("Ingrese número: "))
if primo_compuesto(num):
    print(f"{num} Es Primo. \n Valores divisibles: {get_list_primos(num)}")
else:
    print(f"{num} Es compuesto. \n Valores divisibles: {get_list_primos(num)}")



print("\nFactorización prima de un valor factorial")

numero = int(input("Ingrese valor para calcular su factorización prima: "))
if primo_compuesto(Factorial(numero)):
     print(f"{Factorial(numero)}!  Es primo.")
else:
     print(f"{Factorial(numero)}!  Es compuesto.")


print("\nCalcular promedio")
list_notas = []
i = 3
while i == 3:
    nota = float(input("Ingrese nota: "))
    list_notas.append(nota)
    fin = int(input("Fin del proceso ponga 0: "))
    if fin == 0:
        i = 8
print(round(promedio(list_notas), 2))
