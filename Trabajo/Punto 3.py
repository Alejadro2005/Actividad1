import random
tamaño_lista = 100
inicio_rango = 1
fin_rango = 100

lista_aletoria = [random.choice(range(inicio_rango, fin_rango +1)) for _ in range(tamaño_lista)]

print(lista_aletoria)