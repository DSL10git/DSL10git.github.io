# Hangman game in Python
import random
import time
words = ("apple", "house", "smile", "light", "cloud", "dream", "heart", "happy", "water", "green",
"peace", "music", "lucky", "world", "faith", "truth", "power", "dance", "ocean", "magic",
"grace", "smart", "shine", "laugh", "quick", "brave", "sweet", "movie", "plant", "stone",
"beauty", "trust", "earth", "loved", "think", "clear", "royal", "coast", "sharp", "space",
"flash", "bread", "joint", "style", "begin", "grand", "voice", "super", "class", "order",
"float", "title", "catch", "prime", "blend", "north", "south", "bliss", "limit", "storm","flower",
"energy", "simple", "forest", "island", "friend", "silver", "strong", "travel", "family",
"honest", "spirit", "kindle", "bright", "singer", "global", "future", "nature", "winner", "honor",
"vision", "leader", "health", "action", "famous", "cheese", "wonder", "pretty", "memory", "change",
"smiley", "bubble", "yellow", "splash", "silent", "rocket", "joyful", "secure", "wealth", "circle", "hangman")
# dictionary of key:()

hangman_art = {0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o  One last chance - StickManGuy",
                    "/|\\",
                    "/ \\"),
                7: ("|  o Hi,      |",
                    "| /|\\ I'm     |",
                    "| / \\  ALIVE! |")}

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


def display_man(wrong_guesses):
    decorate()
    for line in hangman_art[wrong_guesses]:
        print(line)
    decorate()

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    wait = True  # Initialize 'wait' before using it
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if not wait:  # Fixed to check if 'wait' is False
            print("Waiting skipped")
        else:
            time.sleep(1.0)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        # Simulate any missing rows with placeholders
        row = ""
        if guess == "cheats please":
            password_good = False
            password_used = 0
            while not password_good:
                password_used += 1
                b = input("Password: ")
                if password_used == 3:
                    print("Falid too many times")
                    break
                if b == "dsl":
                    password_good = True
                    print("Welcome")
                    time.sleep(1.0)
                    b = input("What would you like to do? A. see hangmans, B. get answer, C. skip wait, D. see words, E. word sort: ").lower()
                    if b == "a":
                        for i in range(8):
                            for line in hangman_art[i]:
                                print(line)
                            time.sleep(1.0)
                    elif b == "b":
                        print(f"The answer is: {answer}")
                    elif b == "c":
                        wait = False
                        print("Waiting disabled") 
                        decorate() 
                    elif b == "d":
                        print("These are the words that the game is allowed to ask you: ")
                        time.sleep(0.5)
                        print("""
"apple", "house", "smile", "light", "cloud", "dream", "heart", "happy", "water", "green",
"peace", "music", "lucky", "world", "faith", "truth", "power", "dance", "ocean", "magic",
"grace", "smart", "shine", "laugh", "quick", "brave", "sweet", "movie", "plant", "stone",
"beauty", "trust", "earth", "loved", "think", "clear", "royal", "coast", "sharp", "space",
"flash", "bread", "joint", "style", "begin", "grand", "voice", "super", "class", "order",
"float", "title", "catch", "prime", "blend", "north", "south", "bliss", "limit", "storm","flower",
"energy", "simple", "forest", "island", "friend", "silver", "strong", "travel", "family",
"honest", "spirit", "kindle", "bright", "singer", "global", "future", "nature", "winner", "honor",
"vision", "leader", "health", "action", "famous", "cheese", "wonder", "pretty", "memory", "change",
"smiley", "bubble", "yellow", "splash", "silent", "rocket", "joyful", "secure", "wealth", "circle", "hangman"
""")            

                elif b == "e":
                    print("Here are the words sorted(there can be more than 1 in each catigorey)")
                    time.sleep(0.5)
                    print("""
Foods (Thing that you can eat):
    "apple", "bread", "cheese"
Emotions (feelings):
    "smile", "dream", "heart", "happy", "peace", "bliss",
    "loved", "honest", "spirit", "bright", "joyful",
    "wonder", "secure", "honor", "trust"
Nouns (Words representing things, concepts, or people):
    "apple", "house", "smile", "light", "cloud", "dream",
    "heart", "water", "green", "peace", "music", "world",
    "faith", "truth", "power", "dance", "ocean", "magic",
    "grace", "movie", "plant", "stone", "beauty", "trust",
    "earth", "coast", "space", "flash", "bread", "joint",
    "style", "voice", "class", "order", "float", "title",
    "catch", "north", "south", "bliss", "limit", "storm",
    "flower", "energy", "forest", "island", "friend",
    "silver", "travel", "family", "spirit", "singer",
    "future", "nature", "winner", "vision", "leader",
    "health", "action", "cheese", "wonder", "memory",    
    "change", "bubble", "circle", "hangman", "wealth"
                          
Verbs (Words representing actions or states of being):
    "smile", "dream", "shine", "laugh", "begin", "trust",
    "think", "blend", "kindle", "secure", "float", "catch",
    "travel"
                          
Adjectives (Words describing nouns):
    "light", "happy", "lucky", "green", "smart", "quick",
    "brave", "sweet", "clear", "sharp", "royal", "strong",
    "honest", "bright", "global", "pretty", "silent", "yellow",
    "famous", "joyful", "secure", "simple"
                          
Pronouns (Words that replace nouns)
    There are no pronouns in this list, as all words are specific nouns, verbs, or adjectives.

""")
                else:
                    print("Incorrect password")
        
        if guess == "is it a food":
            if answer == "apple" or answer == "bread" or answer == "cheese":
                print("It is a Food!")
            else:
                print("It isn't a food!")
        if guess == "is it a emotion":
            emotions = ["smile", "dream", "heart", "happy", "peace", "bliss", "loved", "honest", "spirit", "bright", "joyful", "wonder", "secure", "honor", "trust"]
            if guess in emotions:
                print("It is a emotion!")
            else:
                print("It isn't a emotion!")


        if guess == "is it a noun":
            nouns = ["apple", "house", "smile", "light", "cloud", "dream",
    "heart", "water", "green", "peace", "music", "world",
    "faith", "truth", "power", "dance", "ocean", "magic",
    "grace", "movie", "plant", "stone", "beauty", "trust",
    "earth", "coast", "space", "flash", "bread", "joint",
    "style", "voice", "class", "order", "float", "title",
    "catch", "north", "south", "bliss", "limit", "storm",
    "flower", "energy", "forest", "island", "friend",
    "silver", "travel", "family", "spirit", "singer",
    "future", "nature", "winner", "vision", "leader",
    "health", "action", "cheese", "wonder", "memory",    
    "change", "bubble", "circle", "hangman", "wealth"]
            if guess in nouns:
                print("It is a noun!")
            else:
                print("It isn't a noun!")

        if guess == "is it a verb":
            verb = ["smile", "dream", "shine", "laugh", "begin", "trust",
"think", "blend", "kindle", "secure", "float", "catch",
"travel"]
            if guess in verb:
                print("It is a verb!")
            else:
                print("It isn't a verb!")

        if guess == "is it a adjective":
            adjective = ["light", "happy", "lucky", "green", "smart", "quick",
"brave", "sweet", "clear", "sharp", "royal", "strong",
"honest", "bright", "global", "pretty", "silent", "yellow",
"famous", "joyful", "secure", "simple"]
            if guess in adjective:
                print("It is a adjective!")
            else:
                print("It isn't a adjective!")
            
        if guess == "helpful tips":
            print("""
============================================================================================
Helpful Tips            by: Daniel
This game works best on computers. (Every game is best on a big screen)
1. Start with common letters                                                      
Try using vowels (a, e, i, o, u) (Every word has a vowel)
If you tried all of these vowels, try these 10 common consonants:
    1. T
    2. N
    3. S
    4. R
    5. L
    6. D
    7. C
    8. M
    9. H
   10. P
2. Focus on Short Words
    Analyze the word’s length and placement of blanks. Shorter words often follow patterns, making them easier to guess.
                  
3. Look for Letter Patterns
    Common combinations like TH, CH, SH, ST, TR, QU, and ING appear often. Guess one letter to uncover part of the pattern.
                  
4. Think About Word Structure
    Words often start with certain letters:
    S, T, or C are common starting consonants.
    Words often end with E, Y, or S.
                  
5. Guess Strategically
    If you guess a letter and it’s correct, think of what letters commonly appear around it. For example:
    If T is in the word, consider guessing H next for combinations like TH.
                  
6. Watch for Repeated Letters
    Some words have double letters like LL, EE, SS, or OO. If the word has spaces that suggest this, guess accordingly.
                  
7. Eliminate Unlikely Letters
    If the word structure doesn’t match certain letters, avoid wasting guesses. For example, Z, Q, and X are rare unless you suspect the word might be unusual.

8. Use Word Families
    If you think of one possible word, consider others in the same category. For example:
    If the category is "animals" and you guess C, it might lead to CAT, COW, or COYOTE.
                  
9. Practice Common Words
Familiarize yourself with commonly used words in games. Simple words like and, the, this, that, and here often pop up.
                  
10. Pay Attention to the Category
    If a category is provided, narrow your guesses based on what fits. For example:
    In a "food" category, guess letters common in food names (A, E, P, R, etc.).
                  
11. Stay Calm and Logical
    Avoid random guessing; think through each letter based on the revealed pattern and remaining options.
                  
12. In game cheats and some helping
if you need more helps, you can type "is it a food", "is it a emotion", "is it a noun", "is it a verb", "is it a adjective"
if you're still stuck, you can type "cheats please", Here's the password "dsl", (lowercase)
then, type b.
                  
"A" - A will give you all the phases of the stickman
"B" - B will give you the answer
"C" - C will skip the waiting 
"D" - D will give you all the words that the game knows
"E" - E will sort the words into nouns, verbs, and etc  
                  
Hopefully these will help you win Hangman!               
============================================================================================                      
""")


            
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            is_running = False
            print("You win!!!")
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lost 😞")
            is_running = False


if __name__ == "__main__":
    main()