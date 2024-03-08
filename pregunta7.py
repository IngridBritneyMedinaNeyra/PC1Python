#1 Solicitamos al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

#2 Menú de opciones
print("\nSeleccione una opción:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta (primer número menos segundo número)")
print("3. Mostrar la multiplicación de los dos números")

#3 Obtenemos la opción del usuario
opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

#4 Realizamos la operación correspondiente según la opción elegida
if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} menos {numero2} es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
else:
    print("Opción inválida. Por favor, elija 1, 2 o 3.")
