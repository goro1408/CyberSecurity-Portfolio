import re

def check_password_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    symbol = re.search(r"[!@#$%^&*()_+-=]", password)

    strength = sum([length, digit, uppercase, lowercase, symbol])

    if strength == 5:
        return "Strong"
    elif 3 <= strength < 5:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    print(f"Password strength: {check_password_strength(password)}")

