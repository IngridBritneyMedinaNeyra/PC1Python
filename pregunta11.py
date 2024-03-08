#1 Definamos la lista original
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

#2 Eliminamos elementos duplicados y mantener el orden de aparición
lista_procesada = list(dict.fromkeys(lista_original))

#3 Mostramos el resultado
print("Lista Original:", lista_original)
print("Lista Procesada:", lista_procesada)
