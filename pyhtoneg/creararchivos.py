with open("primer_archivo_write.txt", 'a') as f:
  f.write("Agregamos una linea mas con append")
f = open("primer_archivo_write.txt", "r")
print(f.read())
f.close()
