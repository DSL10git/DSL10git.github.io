def main():
    operators = ('+', '-', '/', '*', '^', '%')
    operators_str = " ".join(operators)
    a = input(f"Pick a operator {operators_str}: ")
    while a not in operators:
        print(f"Invalid operator")
        a = input(f"Pick a operator {operators_str}: ")

    while True:
        try:
            num1 = float(input("Pick a number: "))
            break
        except ValueError:
            print(f"Invalid number")
    while True:
        try:
            num2 = float(input("Pick another number: "))
            if num2 == 0 and a == "/":
                print("The second number cannot be zero when dividing")
            else:
                break
        except ValueError:
            print(f"Invalid number")


    res = 0
    if a == "+":
        res = num1 + num2
    elif a == "-":
        res = num1 - num2
    elif a == "/":
        res = num1 / num2
    elif a == "*":
        res = num1 * num2
    elif a == "^":
        res = num1 ** num2
    else:
        res = num1 % num2

    q = input("Do you want it to be rounded(y/n): ")
    if q == "y":
        q2 = int(input("How many digits?: "))
        res2 = round(res, q2)
        print(f"Your number is... {res2}!!!")
    else:
        print(f"Your number is... {res}!!!")



def check_inputs(operator, num1, num2, round_digits):
    """
    if operator is good, we pass the operator check
    if num1 is good, we pass the num1 check
    if num2 is good, we pass the num2 check
    if round_digits is good, we pass the round_digits check

    if all checks are passed, we return True and None
    otherwise, we return False and Error message

    """
    operators = ('+', '-', '/', '^', '*', '%')
    check_operator_passed = True
    check_num1_passed = True
    check_num2_passed = True
    check_round_digits_passed = True
    error_message = None
    if operator not in operators:
        error_message = f"Invalid operator"
        check_operator_passed = False
    
    try:
        float(num1)
    except ValueError:
        error_message = "Invalid first number"
        return False, error_message

    try:
        float(num2)
    except ValueError:
        error_message = "Invalid second number"
        return False, error_message

    if num2 == 0 and operator == "/":
        error_message = f"The second number cannot be zero when dividing"
        return False, error_message

    try:
        int(round_digits)
    except ValueError:
        error_message = "Invalid round digits"
        return False, error_message
    
    return True, error_message
    

def compute(operator, num1, num2, round_digits=None):
    """
    Compute the results of num1 and num2 with the operator
    
    if round_digits is None, we do not round
    if round_digits is an integer, we round with round_digits

    return the computed result
    """
    res = 0
    if operator == "+":
        res = num1 + num2
    elif operator == "-":
        res = num1 - num2
    elif operator == "/":
        res = num1 / num2
    elif operator == "*":
        res = num1 * num2
    elif operator == "^":
        res = num1 ** num2
    else:
        res = num1 % num2
    if round_digits == None:
        return res
    else:
        res2 = round(res, round_digits)
        return res2


def html_main(p):
    from pyscript import document

    result = document.querySelector("#result")
    operators = document.querySelectorAll("input[name='operator']")
    found = None
    for operator in operators:
        if operator.checked:
            found = operator
    operator = found

    operator = operator.value
    num1 = document.querySelector("#num1")
    num1 = num1.value
    num2 = document.querySelector("#num2")
    num2 = num2.value
    round_digits = document.querySelector("#round-digits")
    round_digits = round_digits.value

    """
    run check_inputs
    if passed, go to compute and display the result
    otherwise display error message
    """
    passed, error_message = check_inputs(operator, num1, num2, round_digits)

    if passed:
        # Cast input
        num1 = float(num1)
        num2 = float(num2)
        round_digits = int(round_digits)
        result2 = compute(operator, num1, num2, round_digits)
        result.innerText = f"{result2}"
    else:
        result.innerText = f"{error_message}"