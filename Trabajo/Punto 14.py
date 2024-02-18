def calcular_media(lista):
    if not lista:
        return None
    suma_total = sum(lista)
    media = suma_total / len(lista)
    return media

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5]

media_resultante = calcular_media(lista_numeros)

if media_resultante is not None:
    print("La media aritmética de la lista",lista_numeros,"es:",media_resultante)
else:
    print("La lista está vacía.")