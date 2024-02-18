def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y quitar espacios
    return cadena == cadena[::-1]  # comparar

texto_ingresado = input("Ingrese una palabra palindroma: ")

# Determinar y mostrar si es un palíndromo o no
if es_palindromo(texto_ingresado):
    print(texto_ingresado,"es un palíndromo.")
else:
    print(texto_ingresado,"no es un palíndromo.")