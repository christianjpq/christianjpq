def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if (len(s) < 2) or (len(s) > 6):
        return False
    elif (s[0].isalpha() == False) or (s[1].isalpha() == False):
        return False
    elif (s.isalnum() == False):
        return False
    for i in range(len(s) - 1):
         if (s[i].isnumeric() == True) and (s[i+1].isalpha() == True):
            return False
    for j in range(len(s)-1):
        if (s[j] == "0"):
            return False
    else:
        return True






main()
