#1 Definamos la lista de muestra
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

#2 Eliminamos elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]
lista_resultado = [valor for i, valor in enumerate(lista_muestra) if i not in posiciones_a_eliminar]

#3 Mostramos el resultado
print("Lista Original:", lista_muestra)
print("Resultado esperado:", lista_resultado)
