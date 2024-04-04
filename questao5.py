palavra =  input("Insira uma palavra: ")
aux = ""

for x in range(len(palavra), -1, -1, -1):
    aux += palavra[x]

print(aux)