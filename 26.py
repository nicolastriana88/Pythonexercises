import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    user='root',
    password= any,
    host='127.0.0.1',
    database='usuarios',
    port=3306
)

print(conexion)

# Crear cursor
cursor = conexion.cursor()

# Ejecutar la consulta
cursor.execute("SELECT * FROM usuarios")

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir cada fila de resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()


