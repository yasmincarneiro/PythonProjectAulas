texto = "Eu amo Python!"
        #012345012345

print(texto.find("o"))                           #ele mostra o primeiro 'o'
print(texto[texto.find("o")+1:].find("o"))       #ele mostra o segundo 'o'
print(texto.split(" "))                          #separa a string "eu" "amo" "python"