frase_ex = "Hello World!"

print(frase_ex.startswith("Hello"))  # Retorna se a string está no início da outra, "Hello" no início de "Hello World!"

print(frase_ex.endswith("World!"))  # Retorna se a string está no final da outra, "World!" no final de "Hello World!"

print("llo W" in frase_ex) # Retorna se a frase procurada na string foi encontrada ou não

print(frase_ex.count("o")) # Conta a quantidade da frase procurada na string

print(frase_ex.count("Hello")) # Conta a quantidade da frase procurada na string

print(frase_ex.find("l")) # Traz o índice do primeiro caracter da frase procurada na string, se retornar -1 essa frase não existe