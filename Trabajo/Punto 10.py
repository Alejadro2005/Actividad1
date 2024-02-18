import math

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

if numero_ingresado < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado_factorial = math.factorial(numero_ingresado)
    print("El factorial de",numero_ingresado,"es", resultado_factorial)
