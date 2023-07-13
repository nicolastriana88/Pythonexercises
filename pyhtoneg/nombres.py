import random

# Lista de nombres eslavos
nombres_eslavos = ["Ana", "Boris", "Cecilia", "Dimitri", "Elena", "Felipe", "Greta", "Helena", "Ivan", "Jana", "Katarina", "Luka", "Marta", "Nina", "Olga", "Petra", "Rado", "Sofia", "Tomas", "Vlado", "Zora"]

# Lista de nombres japoneses
nombres_japoneses = ["Akira", "Chihiro", "Emiko", "Fumiko", "Haru", "Ichiro", "Jiro", "Kaori", "Makoto", "Naoko", "Osamu", "Rina", "Sakura", "Takashi", "Yoshiko", "Yuki", "Zakuro"]

# Generar nombre aleatorio
nombre_eslavo = random.choice(nombres_eslavos)
nombre_japones = random.choice(nombres_japoneses)
nombre_completo = nombre_eslavo + " " + nombre_japones

# Imprimir nombre generado
print(nombre_completo)
