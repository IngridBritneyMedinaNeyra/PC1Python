# Solicitamos el costo de la comida al usuario
costo_comida = float(input("Ingrese el costo de su comida: S/."))

# Solicitamos el porcentaje de propina al usuario
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15): "))

# Calculamos la cantidad de propina
propina = (porcentaje_propina / 100) * costo_comida

# Mostramos la cantidad de propina
print(f"La propina a dejar es: S/.{propina:.2f}")
