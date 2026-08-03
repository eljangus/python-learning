firstnum = input("first number: ")
operator = input("operator: ")
secondnum = input("second num: ")
firstnum = float(firstnum)
secondnum = float(secondnum)

print(firstnum, operator, secondnum)
check = input("is this correct? (y/n) ")
if check == "y":
    match operator:
        case "-":
            print(firstnum-secondnum)
        case "+":
            print(firstnum+secondnum)
        case "*":
            print(firstnum*secondnum)
        case "/":
            print(firstnum/secondnum)
else:
    print("go kys")
