#1 Solicitamos al usuario la cantidad de shows musicales vistos en el último año
shows_vistos = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

#2 Verificamos si ha visto más de 3 shows y almacenamos el resultado en una variable booleana
ha_visto_mas_de_3 = shows_vistos > 3

#3 Mostramos el resultado en pantalla
print(f"¿Ha visto más de 3 shows musicales? {ha_visto_mas_de_3}")
