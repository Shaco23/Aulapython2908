dia = (input("Qual o dia de hoje?"))
pedidoPizza = int(input("Quantas pizza comprou?"))
pedidoBebida = int(input("Quantas Bebida comprou?"))
pedidoBolo= int(input("Quantas Bolo comprou?"))
pedidoDoce = int(input("Quantas Doce comprou?"))
# Declara variaveis 

diaFesta = 26

pedidominimoPizza = 10
pedidominimoBebida = 12
pedidominimoBolo = 5
pedidominimoDoce = 600

if diaFesta == int:
    print("Ana esta fazendo a compras no dia da festa")
else:
    print("Ana não esta fazendo no dia da festa")
if(pedidoPizza <= pedidominimoPizza):
    print("Ana não comprou pizza suficientes!")
else:
    print("Ana comprou pizza suficientes!")
if(pedidominimoBebida <= pedidoBebida):
    print("Ana comprou mais bebidas do que o necessario")
else:
    print("Ana comprou bebidas na quantidade correta")
if(pedidominimoBolo <= pedidoBolo):
    print("Ana exedeu a compra de bolo")
else:
    print("Ana comprou a quantidade correta de bolo")
if(pedidominimoDoce > pedidoDoce):
    print("Ana não comprou doces suficiente")
else:
    print("Ana comprou doces suficientes")


