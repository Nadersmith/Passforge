import string
import random
import argparse

# Enhanced password strength evaluation function
def password_strength(password):
    score = 0
    if len(password) >= 16:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 5:
        return "Excellent"
    elif score == 4:
        return "Very Strong"
    elif score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak"

# Function to generate custom passwords with various formats
def generate_custom_password():
    firstname = input("First name (Press Enter to skip): ") or ""
    lastname = input("Last name (Press Enter to skip): ") or ""
    hobby = input("What is your hobby? (Press Enter to skip): ") or ""
    birth_year = input("What is your birth year? (Press Enter to skip): ") or ""
    country = input("What is your country? (Press Enter to skip): ") or ""
    length = input("Password length? (Press Enter to skip, default is 12): ") or 12
    attempts = input("Number of attempts? (Press Enter to skip, default is 1): ") or 1

    length = int(length)
    attempts = int(attempts)

    name = firstname.capitalize() or "User"
    name_lower = name.lower()
    passwords = []

    formats = [
        "{name}@{number}",
        "{name}{number}.",
        "{name}.{number}",
        "{name}@{number}{name_lower}",
        "{name}{number}{number}@",
        "{name}-{reversed_number}",
        "#{name_lower}{number}"
    ]

    for _ in range(attempts):
        number = str(random.randint(100, 999999))
        reversed_number = number[::-1]
        fmt = random.choice(formats)
        password = fmt.format(name=name, name_lower=name_lower, number=number, reversed_number=reversed_number)

        # Adjust password length
        if len(password) > length:
            password = password[:length]
        elif len(password) < length:
            extra = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - len(password)))
            password += extra

        passwords.append(password)

    return passwords

# Save password to a file
def save_password_to_file(password):
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')

# Main function
def main():
    parser = argparse.ArgumentParser(description="Password Generator Tool with Strength Evaluation")
    parser.add_argument("--interactive", action="store_true", help="Interact with the user to generate passwords based on inputs")
    args = parser.parse_args()

    if args.interactive:
        passwords = generate_custom_password()

        for i, password in enumerate(passwords):
            print("=" * 40)
            print(f"Password {i + 1}: {password}")
            print(f"Strength: {password_strength(password)}")
            save_password_to_file(password)
    else:
        print("Please use the --interactive option to generate passwords.")

if __name__ == "__main__":
    main()
