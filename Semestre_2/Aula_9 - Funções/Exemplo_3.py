def barra():
 return "*" * 40
print(barra())

def barra(n=40, caractere="*"):
 return n * caractere

print(barra())

print(barra(80, "."))