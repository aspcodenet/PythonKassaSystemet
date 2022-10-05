from product import Product

allProducts = []

def HuvudMeny() -> int:
    print("1. Ny kund")
    print("2. Avsluta")
    selection = int(input(":"))
    return selection

def NyttKvitto(allProducts):
    while True:
        print("KASSA")
        datum = "2002-10-05 13:45:12"
        print(f"KVITTO:{datum}")
        print("kommandon:")
        print("<productid> <antal>")
        print("PAY")
        action = input("Kommando:")
        if action  == "PAY":
            break

while True:
    sel = HuvudMeny()
    if sel == 2:
        break
    elif sel == 1:
        NyttKvitto(allProducts)



