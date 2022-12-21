x, y, z = input("Expression: ").split(" ")

if y == "+":
    resultado = int(x) + int(z)
    print(float(resultado))
elif y == "-":
    resultado = int(x) - int(z)
    print(float(resultado))
elif y == "*":
    resultado = int(x) * int(z)
    print(float(resultado))
elif y == "/":
    if z == "0":
        print("Numbers cannot divide by zero")
    else:
        resultado = int(x) / int(z)
        print("%.1f" % float(resultado))
else:
    print("insert a valid math operator")