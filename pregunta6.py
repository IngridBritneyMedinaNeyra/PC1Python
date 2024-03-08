#1 Solicitamos la edad del cliente
edad_cliente = int(input("Ingrese la edad del cliente: "))

#2 Calculamos el precio de la entrada según la edad
if edad_cliente < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5  # Entre 4 y 18 años pagan $5
else:
    precio_entrada = 10  # Mayores de 18 años pagan $10

#3 Mostramos el precio de la entrada en pantalla
print(f"El precio de la entrada es: S/.{precio_entrada}")
