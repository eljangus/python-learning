print("Welcome to the BMI calculator!")

dictionary = dict()

while True:
    name = str(input("What is your name?: "))
    weight = float(input("What is your weight in kg?: "))
    height = float(input("What is your height in m?: "))
    check = str(input("is that everyone? (yes/no): "))
    bmi = weight / (height**2)
    if check == "yes":
        dictionary[name] = bmi
        for name, bmi in dictionary.items():
            print(name, ":", round(bmi, 2))
        break
    elif check == "no":
        dictionary[name] = bmi
    else:
        raise Exception("""input has to be either "yes" or "no"!""")
