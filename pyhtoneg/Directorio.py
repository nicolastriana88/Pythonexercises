#directorio = "Curso"
#import os #Crear directorio
#os.mkdir("Curso")
#print("Directorio '% s' creado" % directorio)

#import os #borrar directorio
#os.rmdir("Curso") 

import os
directorios = os.listdir("C:Curso") #listar
for file in directorios:
   print(file)