user_guess = int(input("Number = "))

while user_guess > 100:
    print("Smaller than 100!")

    user_guess = int(input("Number = "))

while user_guess < 1:
    print("Higher than 1!")

    user_guess = int(input("Number = "))

print(user_guess)
