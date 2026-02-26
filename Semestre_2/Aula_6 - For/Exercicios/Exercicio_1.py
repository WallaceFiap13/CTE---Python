# Compras = []

# while True:  
#     Item = input("\nDigite o item que deseja incluir na lista de compras (digite 'stop' para sair):\n")
#     if Item == "stop":
#         break
#     Compras.append(Item)
# for x in Compras:
#     print(x)

Lista_item = []
Lista_qtd = []
Contador = 0

while True:
    item = input("\nDigite o item que deseja incluir na lista de compras (digite 'stop' para sair) = ")
    if item == "stop":
         break
    qtd = int(input("\nDigite a quantidade que necessita do item = "))
    Lista_item.append(item)
    Lista_qtd.append(qtd)

print("\n---------- Lista de Compras ----------")
for x in Lista_item:
     print(f"{Lista_item[Contador]} - {Lista_qtd[Contador]}")
     Contador += 1