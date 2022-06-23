#Let's make a shopping type simulator with a discount if the user buy something again after purchasing an item.

def copy():
    # instead of writing everything over again ill just paste it here and copy it whenever i need.
    if choice in ("1", "2", "3", "4", "5"):
        item_cost = []
        item_list = []

    item_cost.append()
    item_list.append("")

    print("Alright here's the total cost of your items:")
    print(str(sum(item_cost)) + "$")
    print(f"{3 - item_cost[0]} $ is your rest money")
    receipt = input("Would you like a receipt?")
    if (receipt == "y"):
        print(f"You've brought {item_list} for {item_cost} $.")
        print("Have a nice day!!")
    else:
        print("Have a nice day!!")

def meat():
    print("This is what we currently have in stock:")
    print("""1.Steak - 2.30$
2.Chicken - 2.50$
3.Pork - 2.67$
4.Turkey - 2.70$
5.Lamb - 1.99$""")
    purchase = input("What would you like to buy?")
    if purchase in ("1", "2", "3", "4", "5"):
        item_list = []
        item_cost = []
        if (purchase== "1"):
            item_cost.append(2.90)
            item_list.append("Steak")
        elif (purchase == "2"):
            item_cost.append(2.50)
            item_list.append("Chicken")
        elif(purchase == "3"):
            item_cost.append(2.67)
            item_list.append("Pork")
        elif(purchase == "4"):
            item_cost.append(2.70)
            item_list.append("Turkey")
        elif(purchase == "5"):
            item_cost.append(1.99)
            item_list.append("Lamb")
        print("Alright here's the total cost of your items:")
        print(str(sum(item_cost)) + "$")
        print(f"{3 - item_cost[0]} $ is your rest money")
        receipt = input("Would you like a receipt?")
        if (receipt == "y"):
            print(f"You brought {item_list} for {item_cost} $.")
            print("Have a nice day!!")
        else:
            print("Have a nice day!!")
    else:
        print("Invalid input. Please put in the asked information.")

def veggie():
    print("This is what we currently have in stock:")
    print("""1.Lettuce - 1.20$
2.Carrots - 2.20$
3.Cucumber - 1.0$
4.Broccoli - 2.0$
5.Corn - 2.69$""")
    purchase = input("What would you like to buy?")
    if purchase in ("1", "2", "3", "4", "5"):
        item_list = []
        item_cost = []
        if (purchase== "1"):
            item_cost.append(1.20)
            item_list.append("Lettuce")
        elif (purchase == "2"):
            item_cost.append(2.20)
            item_list.append("Carrots")
        elif(purchase == "3"):
            item_cost.append(1.0)
            item_list.append("Cucumber")
        elif(purchase == "4"):
            item_cost.append(2.0)
            item_list.append("Broccoli")
        elif(purchase == "5"):
            item_cost.append(2.69)
            item_list.append("Corn")
        print("Alright here's the total cost of your items:")
        print(str(sum(item_cost)) + "$")
        print(f"{3 - item_cost[0]} $ is your rest money")
        receipt = input("Would you like a receipt?")
        if (receipt == "y"):
            print(f"You've brought {item_list} for {item_cost} $.")
            print("Have a nice day!!")
        else:
            print("Have a nice day!!")

    else:
        print("Invalid input. Please put in the asked information.")

def spices():
    print("This is what we currently have in stock:")
    print("""1.Salt - 0.59$
2.Pepper - 0.59$
3.Cinnamon - 0.69$
4.Oregano - 0.69$
5.Thyme - 0.60$""")
    choice = input()
    if choice in ("1", "2", "3", "4", "5"):
        item_cost = []
        item_list = []
        if (choice == "1"):
            item_cost.append(0.59)
            item_list.append("Salt")
        elif (choice == "2"):
            item_cost.append(0.59)
            item_list.append("Pepper")
        elif (choice == "3"):
            item_cost.append(0.69)
            item_list.append("Cinnamon")
        elif (choice == "4"):
            item_cost.append(0.69)
            item_list.append("Oregano")
        elif (choice == "5"):
            item_cost.append(0.60)
            item_list.append("Thyme")
        print("Alright here's the total cost of your items:")
        print(str(sum(item_cost)) + "$")
        print(f"{3 - item_cost[0]} $ is your rest money")
        receipt = input("Would you like a receipt?")
        if (receipt == "y"):
            print(f"You've brought {item_list} for {item_cost} $.")
            print("Have a nice day!!")
        else:
            print("Have a nice day!!")
    else:
        print("Invalid input. Please put in the asked information.")

def fruits():
    print("This is what we currently have in stock:")
    print("""1.Apples - 1.10$
2.Pears - 0.90$
3.Watermelon - 1.29$
4.Banana - 0.80$
5.Avocado - 0.70$""")
    choice = input()
    if choice in ("1", "2", "3", "4", "5"):
        item_cost = []
        item_list = []
        if (choice == "1"):
            item_cost.append(1.10)
            item_list.append("Apples")
        elif(choice == "2"):
            item_cost.append(0.90)
            item_list.append("Pears")
        elif(choice == "3"):
            item_cost.append(1.29)
            item_list.append("Watermelon")
        elif(choice == "4"):
            item_cost.append(0.80)
            item_list.append("Banana")
        elif(choice == "5"):
            item_cost.append(0.70)
            item_list.append("Avocado")
        print("Alright here's the total cost of your items:")
        print(str(sum(item_cost)) + "$")
        print(f"{3 - item_cost[0]} $ is your rest money")
        receipt = input("Would you like a receipt?")
        if (receipt == "y"):
            print(f"You've brought {item_list} for {item_cost} $.")
            print("Have a nice day!!")
        else:
            print("Have a nice day!!")
    else:
        print("Invalid input. Please put in the asked information.")

def bread():
    print("This is what we currently have in stock:")
    print("""1.Sandwich Bread - 0.40$
2.Hamburger Buns - 0.99$
3.Baguette - 1.0$
4.Rye Bread - 0.60$
5.Cornbread - 0.89$""")
    choice = input()
    if choice in ("1", "2", "3", "4", "5"):
        item_cost = []
        item_list = []
        if (choice == "1"):
            item_cost.append(0.40)
            item_list.append("Sandwich Bread")
        elif(choice == "2"):
            item_cost.append(0.99)
            item_list.append("Hamburger Buns")
        elif(choice == "3"):
            item_cost.append(1.0)
            item_list.append("Baguette")
        elif(choice == "4"):
            item_cost.append(0.60)
            item_list.append("Rye Bread")
        elif(choice == "5"):
            item_cost.append(0.89)
            item_list.append("Cornbread")
        print("Alright here's the total cost of your items:")
        print(str(sum(item_cost)) + "$")
        print(f"{3 - item_cost[0]} $ is your rest money")
        receipt = input("Would you like a receipt?")
        if (receipt == "y"):
            print(f"You've brought {item_list} for {item_cost} $.")
            print("Have a nice day!!")
        else:
            print("Have a nice day!!")
    else:
        print("Invalid input. Please put in the asked information.")

def shop():
    if (choice == "y"):
        print("""These are our sections:
1.Meat section
2.Vegetables section
3.Spices section
4.Fruits section
5.Bread section
Where would you like to buy?""")
        section = input()
        if section in ("1", "2", "3", "4", "5"):
            if (section == "1"):
                meat()
            elif (section == "2"):
                veggie()
            elif(section == "3"):
                spices()
            elif(section == "4"):
                fruits()
            elif(section == "5"):
                bread()
    elif (choice == "n"):
        print("Have a good day!!")
    else:
        print("Invalid input. Please put in the asked information.")

#Let's do this
print("Today you have to go grocery shopping but you notice that you only have 3$ with you. You can only make one purchase.")
choice = input("Welcome to the market! Would you like to buy anything? (y/n)")
shop()