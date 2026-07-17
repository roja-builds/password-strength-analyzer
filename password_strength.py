def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add a number")

    if any(char in "!@#$%^&*()_+-=" for char in password):
        score += 1
    else:
        feedback.append("Add a special character (!@#$%^&*)")

    levels = {0: "Very Weak", 1: "Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
    return levels[score], feedback


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, tips = check_password_strength(pwd)
    print(f"\nPassword Strength: {strength}")
    if tips:
        print("Suggestions to improve:")
        for tip in tips:
            print(f"- {tip}")
