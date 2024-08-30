import math 
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operador = input("Introduce el numero de la operación a realizar (suma(1), resta(2), multiplicación(3), división(4), potencia(5), radicacion(6)): ".lower())
suma=1
resta=2
multiplicación=3
division=4
potencia=5
radicacion=6
if operador == '1':
    resultado = num1 + num2
    print("El resultado es", resultado)
elif operador == '2':
    resultado = num1 - num2
    print("El resultado es", resultado)
elif operador == '3':
    resultado = num1 * num2
    print("El resultado es", resultado)
elif operador == '4':
    resultado = num1 / num2
    print("El resultado es", resultado)
elif operador == '5':
    resultado = num1 ** num2
    print("El resultado es", resultado)
elif operador == '6':
    if num2 > 0:
        resultado = num1 ** (1 / num2)
        print(f"El resultado de la raíz {num2} de {num1} es", resultado)
    else:
        print("Error: El segundo número debe ser mayor que 0 para calcular la raíz")
else:
    print("Operación no válida. Por favor, elige un número del 1 al 6.")