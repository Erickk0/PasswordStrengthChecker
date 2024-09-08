import re

def check_pw_strength(password):

    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W]', password) is not None

    score = 0

    if length_criteria:
        score += 1
    if upper_criteria:
        score += 1
    if lower_criteria:
        score += 1
    if digit_criteria:
        score += 1


    if score == 5:
        print("Password is strong")
    if score < 5:
        print("Password is OK")
    if score < 2:
        print("Password is weak")