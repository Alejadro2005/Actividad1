def calcular_suma(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso
lista_numeros = [1,3,4,6]

suma_resultante = calcular_suma(lista_numeros)

print("La lista es", lista_numeros, "y la suma es", suma_resultante)