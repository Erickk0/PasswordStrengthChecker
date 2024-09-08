import re
from zxcvbn import zxcvbn, feedback


def check_pw_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_criteria = re.search(r'[\W]', password) is not None
    common_patterns = ["12345678", "87654321"]

    score = 0

    if length_criteria:
        score += 1
    if upper_criteria:
        score += 1
    if lower_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1
    if password in common_patterns:
        score = 0  # If password matches a common pattern, score becomes 0.

    return score


def zxcvbn_feedback(password):
    results = zxcvbn(password)
    return results['feedback']


def prompt_password():
    while True:
        password = input("Enter a password: ")
        score = check_pw_strength(password)

        if score == 5:
            print("Password is strong")
            feedback = zxcvbn_feedback(password)
            print("Feedback: ", feedback.get('suggestions'))
            break
        elif score >= 2:
            print("Password is OK")
            feedback = zxcvbn_feedback(password)
            print("Feedback: ", feedback.get('suggestions'), feedback.get('warning'))
            break
        elif score < 2:
            print("Password is weak. Please enter a stronger password.")
        if score == 0:
            print("Password is too weak. Please enter a stronger password.")


prompt_password()
