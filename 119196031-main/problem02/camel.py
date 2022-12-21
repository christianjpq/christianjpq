camelCase = input("camelCase: ")
contador = 0

for caractere in camelCase.strip():
    if caractere.isupper() and contador > 0:
        print("_"+caractere.lower(), end ="")
    elif contador == 0:
        print(caractere.lower(), end="")
    else:
        print(caractere,end="")
    contador += 1
print("")