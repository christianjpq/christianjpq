def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#remove $ e transforma a str em float
def dollars_to_float(d):
    return float(d.strip("$"))

#remove % e divide por 100 o número informado
def percent_to_float(p):
    return float(p.strip("%")) / 100


main()