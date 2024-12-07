import random
num_range = 20
num_tries = 3
play_again = 'y'
input("Welcome to number guessing game! (Click Enter to countinue)")
input(f"You have {num_tries+1} tries, so let's begin (Click enter to countinue)")
while play_again == 'y':
    guess = int(input(f"guess a number from 1 to {num_range}: "))
    num = random.randint(1, num_range)

    for i  in range(num_tries):
        if guess == num:
            print("Congratulations!")
            break
        else:
            num2 = random.randint(0, 2)
            if num2 == 0:
                print(f"You missed!")
            elif num2 == 1:
                print(f"Sorry that's wrong!")
            else:
                print(f"Incorrect!")
            hint = input("Do you need a hint?(y/n): ")
            if hint == "y":
                if num < guess:
                    print("your guess is greater than the answer")
                else:
                    print("your guess is less than the answer")
            guess = int(input(f"You still have {num_tries-i} tries, please try again: "))
    else:
        print(f"The number was {num}!")
    play_again = input("Would like to try again?(y/n): ")
print("Bye!")