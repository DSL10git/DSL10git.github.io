# password generator
import random
import string


def generate_password(min_lengths, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lengths:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return pwd
 

def local_main():
    min_length = int(input("Enter the minimum length for your password: "))
    has_number = input("Do you want to have numbers(y/n): ").lower() == "y"
    has_special = input("Do you want to have special(y/n): ").lower() == "y"
    pwd = generate_password(min_length, has_number, has_special)
    print(f"Your password is... {pwd}")


def html_main(p):
    from pyscript import document

    result = document.querySelector("#result")
    min_length = document.querySelector("#min-length")
    has_num = document.querySelector("#has-num")
    has_special = document.querySelector("#has-special")
    password = generate_password(int(min_length.value), has_num.checked, has_special.checked)
    result.innerText = f"{password}" 
