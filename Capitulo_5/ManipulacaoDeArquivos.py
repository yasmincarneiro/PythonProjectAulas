arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo!\n")

arquivo.close()

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\n'Hakuna Matata")

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nEh lindo dizer!")

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nHakuna Matata")

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nSim, vai entender!'")


with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
     print(linha)

