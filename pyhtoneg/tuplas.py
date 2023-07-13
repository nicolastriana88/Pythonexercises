mitupla= ("piña", "naranja", "limon", "limon", 2023, 2024,1.35)
print(len(mitupla))
print(mitupla[6])

mitupla= ("piña", "naranja", "limon", "limon", 2023, 2024,1.35)
print(mitupla)
milista = list(mitupla)
milista.append("fresa.")
mitupla = tuple(milista)
print(mitupla)

mitupla = ("piña", "naranja", "limon", "limon", 2023, 2024, 1.35, "fresa")
del mitupla
print(mitupla)