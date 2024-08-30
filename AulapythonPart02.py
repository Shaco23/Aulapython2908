#Logica de programação 
#Os operadores lógicos são usados para combinar expressões Boolenas. 

#Data da inscrição e variavel 

dia = (input("Dia da inscricao?"))
diaEspera = (input("Voce esta na lista de espera? (Sim/Nao)"))
CondEspecial = (input("Possui indicacao especial?"))

datainicial = 28

#Codigo da data de inscricao

if datainicial:
    print("Esta dentro da Data de inscricao")
else:
    print("Não não esta dentro da data de inscricao")

diaEsperano = False

if(diaEspera.upper() == "sim".upper()):
    diaEspera = True
elif(diaEspera.upper() == "Nao".upper() or diaEspera.upper() == "Nao"):
    diaEspera = False
else:
    print("Não foi digitado corretamente a pergunta da lista de espera")

#codigo da lista de espera 

if not diaEspera:
    print("Marcelo não esta na lista de espera")
else:
    print("Marcelo esta na lista de espera")


if not CondEspecial:
    print("Maecelo tem indicacao especial")
else:
    print("Nao tem indicacao especial")