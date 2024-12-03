import string

def validate(email):
    # cond1: must have exactly 1 @
    count = 0
    for i in email:
        if i == "@":
            count += 1

    # add condition to valid
    if count != 1:
        return False

    # get recipient name
    recipient = email[:email.index("@")]

    # cond2: recipient has 3-24 chars
    if len(recipient) < 3 or len(recipient) > 24:
        return False

    # cond3: recipient must contain only
    # letters or digits or special char - . and _
    # hint: for loop
    # create a string that contain all
    # the valid chars
    valid_chars = string.ascii_letters + string.digits + "-._"
    for char in recipient:
        if char not in valid_chars:
            return False

    # cond4: A special character cannot appear as the first or last character in an email address.
    if email[0] in "-._":
        return False
    if email[-1] in "-._":
        return False

    # check domain name
    domain = email[email.index("@")+1:]
    if "." not in domain:
        return False
    domain = domain[:domain.index(".")]

    # cond: 
    # a maximum of 12 characters and minimum of 3 characters
    if len(domain) < 3 or len(domain) > 12:
        return False

    # cond2:
    # Uppercase and lowercase letters in English (A-Z, a-z)
    # Digits from 0 to 9
    # A hyphen (-)
    valid_chars2 = string.ascii_letters + string.digits + "-"
    for i in domain:
        if i not in valid_chars2:
            return False

    # check top-level domain name
    # hint 123@gmail.com -> com is the top-level domain
    # com is the one after "."
    top_level_domain = email[email.index("@")+1:]
    top_level_domain = top_level_domain[top_level_domain.index(".")+1:]

    # cond1: top-level domain name should be one of these
    # com, net, org, tech
    if top_level_domain not in ("com", "net", "org", "tech", "io"):
        return False

    return True

if __name__ == "__main__":
    # write code here
    email = input("Enter email: ")
    is_valid = validate(email)
    if is_valid:
        print("Email is valid")
    else:
        print("Email is invalid")