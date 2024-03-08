#1 Solicitamos al usuario el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

#2 Obtenemos la extensión del archivo (sufijo) en minúsculas
extension = nombre_archivo.lower().split('.')[-1]

#3 Definimos el diccionario de extensiones y sus tipos MIME correspondientes
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'
}

#4 Obtenemos el tipo MIME correspondiente o 'application/octet-stream' si no se encuentra
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

#5 Mostramos el resultado
print(f"Tipo MIME para '{nombre_archivo}': {tipo_mime}")
