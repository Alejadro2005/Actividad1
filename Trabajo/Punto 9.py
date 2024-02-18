import random
filas = 3
columnas = 4
inicio_rango = 1
fin_rango = 10

matriz_generada = [[random.randint(inicio_rango, fin_rango) for _ in range(columnas)] for _ in range(filas)]

print("Matriz generada:")
for fila in matriz_generada:
    print(fila)