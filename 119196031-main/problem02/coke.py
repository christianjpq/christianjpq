debito = 50

while debito > 0:
    print("Amount due: ", debito)
    moeda = int(input("Insert coin: "))

    if (moeda == 5) or (moeda == 10) or (moeda == 25):
        debito = debito - moeda
        
        if (debito < 0):
            print("Change owed:", (debito * -1))
            break
        elif (debito == 0):
            print("Change Owed: 0")
