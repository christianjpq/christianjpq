resp = input("What is the Awser to Great Question of Life, the Universe and Everything? ")


match resp.strip().lower():
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
