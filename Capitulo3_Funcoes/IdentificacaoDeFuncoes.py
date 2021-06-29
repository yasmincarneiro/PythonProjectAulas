#def <identificador da funcao> (<parametro(s)>):
#	<código que será executado>
#	return <Dado que será retornado, caso seja necessário>

def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite " + resp + " para continuar: ").upper()