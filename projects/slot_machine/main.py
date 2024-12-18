# Python Slot Machine
import random
import time
def spin_row():
    symbols = ["💀", "🍒", "🍉", "🍋", "🔔", "⭐️", "🌟💫✨SUPER🌠STAR!🌟💫✨"]

    return [random.choice(symbols) for _ in range(3)]

def decorate(a=None):
    if a is None:
        a = random.randint(1, 4)
    if a == 1:
        print("***********************")
    elif a == 2:
        print("-----------------------")
    elif a == 3:
        print("#######################")
    elif a == 4:
        print("=======================")
    else:
        print(a * 15)
    return a

def print_row(row, decorator):
    decorate(decorator)
    print("|".join(row))
    decorate(decorator)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🔔":
            return bet * 4
        elif row[0] == "⭐️":
            print("Good Job!")
            return bet * 5
        elif row[0] == "🌟💫✨SUPER🌠STAR!🌟💫✨":
            print("Jack Pot💯!!!💯")
            return bet * 1000
        elif row[0] == "💀":
            print("Only word: 💀💀💀💀💀💀💀")
            return -100000000
    return 0
        

def main():
    easter_egg_used = False
    wait = True
    balance = 100
    a = decorate()
    print("Welcome to Spin & Win")
    print("symbols: ??? 🍒 🍉 🍋 🔔 ⭐️ ???")
    decorate(a)

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ").lower()
        if easter_egg_used and (bet == "pizza" or bet == "ice cream"):
            print("Sorry, but you have used your easter egg")
        else:
            b = random.randint(1, 2)
            if bet == "pizza":
                easter_egg_used = True
                a = "🍕"
                print("Pizza easter egg activated")
                decorate(a)
            elif bet == "help":
                print("If you want to know the easter egg, type 'see easter egg', to exit type 'exit', type 'SUPER secret' to learn some secrets!")
            elif bet == "super secret":
                print("type 'cheat mode' and you will need a password! The password is 'dsl', DO NOT CLICK CRASH!!! it will crash the game")
            elif bet == "see easter egg":
                print("The secret easter eggs are ice cream and pizza, you can only add it once but if you use this command 'clear easter egg' you can print more, if you want to exit, for more info, type 'help'")
            elif bet == "clear easter egg" and easter_egg_used == True:
                easter_egg_used = False
                print("Easter egg cleared!")
            elif bet == "clear easter egg" and easter_egg_used == False:
                print("You don't have any easter eggs!")
            elif bet == "exit":
                print("Bye!")
                exit()
            elif bet == "cheat mode":
                password_good = False
                password_used = 0
                while password_good == False:
                    password_used += 1
                    b = input("Password: ")
                    if password_used == 3:
                        print("used too many times")
                    if b == "dsl":
                        password_good = True
                        print("Good...")
                        time.sleep(1.0)
                        print("Hello, creator")
                        time.sleep(1.0)
                        c = input("So, what do you need? A. No waiting, B. More money C. get in a row, D. Crash: ").lower()
                        if c == "a":
                            wait = False
                            print("Waiting disabled") 
                            decorate(a)   
                        if c == "b":
                            d = int(input("How much?: "))
                            print(d)
                            balance += d
                            print(f"your money")
                            decorate(a)
                        if c == "c":
                            e = input('which ones?"💀"(death), "🍒"(Cherry), "🍉"(Watermelon), "🍋"(lemon), "🔔"(bell), "⭐️"(star), "🌟💫✨SUPER🌠STAR!🌟💫✨"(special one): ').lower()
                            if e == "cherry":
                                print("🍒|🍒|🍒")
                                balance *= 3
                            elif e == "watermelon":
                                print("🍉|🍉|🍉")
                                balance *= 3
                            elif e == "lemon":
                                print("🍋|🍋|🍋")
                                balance *= 4
                            elif e == "bell":
                                print("🔔|🔔|🔔")
                                balance *= 5
                            elif e == "star":
                                print("⭐️|⭐️|⭐️")
                                print("Good Job!")
                                balance *= 10
                            elif e == "special one":
                                print("🌟💫✨SUPER🌠STAR!🌟💫✨|🌟💫✨SUPER🌠STAR!🌟💫✨|🌟💫✨SUPER🌠STAR!🌟💫✨")
                                print("Jack Pot💯!!!💯")
                                balance *= 1000
                            elif row[0] == "death":
                                print("💀|💀|💀")
                                print("Only word: 💀💀💀💀💀💀💀")
                                balance = -10000000128476523948572649857623984756293847562938475629384756298347652983746592837465928745692384756239847

                        if c == "d":
                            for i in range(40):
                                print("OH NOOO!!! ")
                            f = input("ARE YOU SURE!?!😰😰😰(y/n):")
                            if f == "y":
                                print("NOOOOØ00😰😰😰")
                                time.sleep(1.0)
                                for i in range(10000):
                                    print("I'M GOING TO CRASH!!! ")
                                
                            else:
                                print("Few!")
            elif bet == "ice cream":
                easter_egg_used = True
                if b == 1:
                    a = "🍦"
                    print("Ice cream easter egg activated")
                    decorate(a)
                else:
                    a = "🍨"
                    print("Ice cream easter egg activated")
                    decorate(a)
            else:
                if not bet.isdigit():
                    print("Please enter a valid amount!")
                    continue

                bet = int(bet)

                if bet > balance:
                    print("Insufficient funds")
                    continue

                if bet <= 0:
                    print("Bet must be greater than 0")
                    continue
                balance -= bet
                
                row = spin_row()
                print("Spinning..\n")
                if wait == False:
                    print("Waiting skipped")
                else:
                    time.sleep(1.0)
                print_row(row, decorator=a)

                payout = get_payout(row, bet)

                if payout > 0:
                    print(f"You won ${payout}")
                else:
                    print("Sorry you lost this round")

                    balance += payout
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again != "y":
                    break
            
    decorate(a)        
    print(f"Game over! Your final balance is ${balance}")
    decorate(a)
if __name__ == "__main__":

    main()