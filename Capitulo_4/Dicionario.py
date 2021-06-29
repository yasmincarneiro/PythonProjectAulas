usuarios = {}
print (usuarios)

usuarios = {
    "Chaves" : ["Chaves do 8", "24/12/2020", "Recepcao_01"],
    "Quico": ["Quico das Flores", "20/12/2020", "Recepcao_02"]
}
print(usuarios)

usuarios["Florinda"] = {"Dona Florinda", "17/12/2020", "Recepcao_03"}

print(usuarios)

print("###-----------###")

print(usuarios.get("Quico"))