while True:
    try:
        entrada = input("Fraction: ").strip()
        antes, depois = entrada.split("/")
        y = int(antes)
        z = int(depois)
        if y <= z:
            x = (int(y) / int(z)) * 100
            if x > 98 and x <= 100:
                print("F")
                break
            elif x <= 1 and x >= 0:
                print("E")
                break
            elif x < 99 and x > 1:
                print("%0.f"%x, "%", sep="")
                break
    except (ValueError, ZeroDivisionError):
        pass
