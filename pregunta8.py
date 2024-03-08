# Solicitar al usuario una hora en formato HH:MM
hora_usuario = input("Ingrese la hora en formato HH:MM: ")

# Dividir la entrada en horas y minutos
horas, minutos = map(int, hora_usuario.split(":"))

# Verificar si la hora está dentro del rango de desayuno, almuerzo o cena
if 7 <= horas < 8:
    print("Es hora de desayunar.")
elif 12 <= horas < 13:
    print("Es hora de almorzar.")
elif 18 <= horas < 19:
    print("Es hora de cenar.")
else:
    # No es hora de comer, no se envía nada
    pass
