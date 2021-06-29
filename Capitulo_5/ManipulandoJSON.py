import json

dicionario = {

  "Chaves": ["Chaves do 8", "24/12/2020", "Recepcao_01"],
  "Quico": ["Quico das Flores", "20/12/2020", "Recepcao_02"],
  "Florinda": ["Dona Florinda", "17/12/2020", "Recepcao_03"]

}
with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)
