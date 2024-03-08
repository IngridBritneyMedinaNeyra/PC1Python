#1 Solicitamos el número de payasos y muñecas vendidos
payasos = int(input("Ingrese el número de payasos vendidos: "))
munecas = int(input("Ingrese el número de muñecas vendidas: "))

#2 Definimos el peso de cada payaso y muñeca en gramos
peso_payaso = 112
peso_muneca = 75

#3 Calculamos el peso total del paquete
peso_total = (payasos * peso_payaso) + (munecas * peso_muneca)

#4 Mostramos el peso total del paquete
print(f"El peso total del paquete es: {peso_total} gramos")