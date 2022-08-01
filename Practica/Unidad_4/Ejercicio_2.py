# Ejercicio 2
while True:
    age = input("Buy a ticket, please enter your age: \n>> ")

    if age == "quit":
        print("Thank you for your purchase")
        break

    try:
        if (int(age) > 0) and (int(age) < 5):
            print("Free ticket")
        elif (int(age) >= 5) and (int(age) < 9):
            print("Ticket price: U$s 15")
        elif (int(age) >= 9) and (int(age) < 14):
            print("Ticket price: U$s 23")
        elif (int(age) >= 14) and (int(age) < 100):
            print("Ticket price: U$s 35")
        else:
            print("You are awesome!! Free ticket for you")

    except ValueError:
        print("You can't enter letters. Just numbers greater 0")

# Ver por que cuando le pasas un numero negativo lo toma en lugar de dar un error
