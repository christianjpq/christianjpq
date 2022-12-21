sentenca = input("Input: ")
print("Output: ", end="")

for letras in sentenca:
        print(letras.strip("aeiouAEIOU"), end="")
print("")
