from zeep import Client

client = Client('http://localhost:8000')

#Suma de dos números
num1 = 10
num2 = 20
result_suma_dos_numeros = client.service.SumaDosNumeros(num1, num2)
print(f"La suma de {num1} y {num2} es:", result_suma_dos_numeros)

#Resta de  dos números
num3 = 20
num4 = 5
result_resta_dos_numeros = client.service.RestaDosNumeros(num3, num4)
print(f"La resta de {num3} y {num4} es:", result_resta_dos_numeros)

#Multiplicación de dos números
num5 = 9
num6 = 10
result_multiplicacion_dos_numeros = client.service.MultiplicacionDosNumeros(num5, num6)
print(f"La multiplicación de {num5} y {num6} es:", result_multiplicacion_dos_numeros)

#División de dos números
num7 = 40
num8 = 2
result_division_dos_numeros = client.service.DivisionDosNumeros(num7, num8)
print(f"La división de {num7} entre {num8} es:", result_division_dos_numeros)
