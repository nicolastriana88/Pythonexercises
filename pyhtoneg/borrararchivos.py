##import os
##os.remove("prueba.txt")

import os
directorios = os.listdir("C:Curso Python")
for file in directorios:
   print(file)