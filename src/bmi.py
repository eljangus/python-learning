def fatty(name, weight, height):
    BMI = weight / (height*height)
    if BMI >= 25:
        print(name, "du bist ein Fettsack! Dein BMI beträgt:", BMI)
    elif BMI <= 25 and BMI >= 18.5:
        print(name, "du bist gesund! Dein BMI beträgt:", BMI)
    elif BMI <= 18.5:
        print(name, "du bist ein Stock! Dein BMI beträgt:", BMI)
    return BMI, name


fatty(input("Wie lautet dein Name?: "), float(input("Was ist dein Gewicht in kg?: ")), float(input("Was ist deine Größe in m?: ")))
