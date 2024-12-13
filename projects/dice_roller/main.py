import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",  
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",  
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",  
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",  
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",  
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",  
        "│  ●   ●  │",
        "└─────────┘")

}
dice = []
total = 0
success = False
while not success:
    try:
        num_of_dice = int(input("How many dices?: "))
        if num_of_dice > 10:
            print("too much!")
            success = False
        elif num_of_dice < 1:
            print("too small!")
            success = False
        else:
            success = True
    except:
        print("Error, invalid input!")

ver_or_not = input("Do you want it to be verticle or horizontal?(v/h):")
if ver_or_not == "v":
    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))

    for die in range(num_of_dice):
        for line in dice_art.get(dice[die]):
            print(line)

    for die in dice:
        total += die
    print(f"total: {total}")
else:
    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total += die
    print(f"total: {total}")