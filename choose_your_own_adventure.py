name = input("Type your name: ").title()
print(f"Hello {name}, Welcome to this adventure!")

answer = input("You are on a dirt road, it has come to and end and you can go left or right, which way would you like to go? ").lower()

if answer == "left":
    answer = input("You arrive at a river, would you like to swim across it?\n Type swim or walk: ").lower()

    if answer == "swim":
        print("A hungry alligator caught you in a death roll, rip!")
    elif answer == "walk":
        print("You walked into quicksand and died!")
    else:
        print("Not a valid option, you died!")

elif answer == "right":
    answer = input("You come to a wobbly bridge, would you like to cross it or head back?\n Type cross or back: ").lower()

    if answer == "back":
        print("You went back and stepped on a landmine!")
    elif answer == "cross":
        answer = input("You cross the bridge and see a stranger.\nWould you like to talk to him?\nType yes or no: ").lower()
        if answer == "yes":
            print("The stranger is on an adventure to give away prizes!\nYOU WIN!")
        elif answer == "no":
            print("You ignore the stranger avoiding eye contact.\nYOU LOSE!")
        else:
            print("Not a valid option, you died!")
else:
    print("Not a valid option, you died!")

print(f"Thank you for playing, {name}!")