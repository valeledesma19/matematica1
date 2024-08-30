num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operador = input("Introduce el numero de la operación a realizar (suma(1), resta(2), multiplicación(3), división(4)): ".lower())
suma=1
resta=2
multiplicación=3
division=4
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
