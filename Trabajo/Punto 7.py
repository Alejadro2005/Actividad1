def encontrar_numero(lista):
    if not lista:
        return None, None

    maximo = minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo


# Ejemplo de uso
lista_numeros = [13, 8, 5, 7, 80, 90]

maximo, minimo = encontrar_numero(lista_numeros)

print("El número más grande en la lista es:",maximo)
print("El número más pequeño en la lista es:",minimo)