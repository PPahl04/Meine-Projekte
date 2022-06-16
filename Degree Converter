#I`ll try making a converter for various things.

def printin():
    print("This program is a converter for degrees.")
    print("Please select one of the following degrees:")
    print("1.Kelvin")
    print("2.Fahrenheit")
    print("3.Celsius")

def kelvin(degree):
    print("Enter the temperature:")
    num = float(input())
    print(f"What should {degree} be converted to?")
    second_degree = input()
    # into Fahrenheit
    if (second_degree == "Fahrenheit","F"):
        Kelvin_To_Fahrenheit = (num - 273.15) * 9 / 5 + 32
        print(f"{num} {degree} would be {Kelvin_To_Fahrenheit} {second_degree}")
        # into Celsius
    if (second_degree == "Celsius"):
        Kelvin_To_Celsius = num - 273.15
        print(f"{num} {degree} would be {Kelvin_To_Celsius} {second_degree}")

def fahrenheit(degree):
    print("Enter the temperature:")
    num = float(input())
    print(f"What should {degree} be converted to?")
    second_degree = input()
    if (second_degree == "Kelvin"):
        Fahrenheit_To_Kelvin = (num - 32) * 5 / 9 + 273.15
        print(f"{num} {degree} would be {Fahrenheit_To_Kelvin} {second_degree}")
    if (second_degree == "Celsius"):
        Fahrenheit_To_Celsius = (num - 32) * 5 / 9
        print(f"{num} {degree} would be {Fahrenheit_To_Celsius} {second_degree}")

def celsius(degree):
    print("Enter the temperature:")
    num = float(input())
    print(f"What should {degree} be converted to?")
    second_degree = input()
    if (second_degree == "Kelvin"):
        Celsius_To_Kelvin = num + 273.15
        print(f"{num} {degree} would be {Celsius_To_Kelvin} {second_degree}")
    if (second_degree == "Fahrenheit"):
        Celsius_To_Fahrenheit = (num * 9 / 5) + 32
        print(f"{num} {degree} would be {Celsius_To_Fahrenheit} {second_degree}")

def converter():
    choice = input("Do you want to tryout this converter???")
    if (choice == "Yes","yes","sure","yeah","y","Y"):
      printin()
      degree = input()
      #User wants to convert Kelvin
      if (degree == "Kelvin","kelvin"):
        kelvin(degree)
      #User wants to convert Fahrenheit
      elif (degree == "Fahrenheit","fahrenheit"):
        fahrenheit(degree)
      elif (degree == "Celsius","celsius"):
        celsius(degree)
    else:
      print("Bro what the fuck????")

converter()

