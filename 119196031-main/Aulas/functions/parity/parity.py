def main():
    x = int(input("Digite o valor de x: "))
    if is_even(x):
        print("é par")
    else:
        print("é impar")

def is_even(n):
   return n % 2 == 0


main()