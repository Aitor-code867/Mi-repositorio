print("Calculadora")

# Solicitar los números iniciales
num1 = int(input("Da el primer número: "))
num2 = int(input("Da el segundo número: "))

while True:
    # Mostrar el menú
    print("\n(1) +")
    print("(2) -")
    print("(3) * ")  # Corregido para multiplicación
    print("(4) /")
    print("(5) Cambiar números")
    print("(6) Salir")
    print(f"Números actuales: {num1} {num2}")

    # Solicitar la opción del usuario
    opcion = input("Selecciona algo (1-6): ")

    if opcion == '1':
        resultado = num1 + num2
        print(f"El resultado es: {resultado}")
    elif opcion == '2':
        resultado = num1 - num2
        print(f"El resultado es: {resultado}")
    elif opcion == '3':
        resultado = num1 * num2  # Corregido para multiplicación
        print(f"El resultado es: {resultado}")
    elif opcion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif opcion == '5':
        num1 = float(input("Da el primer número: "))
        num2 = float(input("Da el segundo número: "))
    elif opcion == '6':
        print("¡Gracias!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")