score = 0
questions = 4

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").title()

if playing != "Yes":
    print("Maybe next time!")
    quit()

print("Okay! Let's play :D")

answer = input("What does CPU stand for? ").title()

if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect!")
    print(score)

answer = input("What does GPU stand for? ").title()

if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect!")
    print(score)

answer = input("What does RAM stand for? ").title()

if answer == "Random Access Memory":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect!")
    print(score)

answer = input("What does PSU stand for? ").title()

if answer == "Power Supply Unit":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Incorrect!")
    print(score)

if score == questions:
    print(f"You got all {score} questions correct!")
else:
    print(f"You got {score} out of {questions} questions correct!")