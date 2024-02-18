num1 = float(input("ingrese numero1:"))
num2 = float(input("ingrese numero2:"))

def sumar():
    resultado = num1 + num2
    return resultado


def restar():
    resultado = num1 - num2
    return resultado


def multiplicar():
    resultado = num1 * num2
    return resultado


def division():
    if num2 != 0:
        resultado = num1 / num2
        return resultado

    else:
        return "NO es posible dividir por cero."

print("Suma",sumar())
print("resta",restar())
print("multiplicacion",multiplicar())
print("division",division())