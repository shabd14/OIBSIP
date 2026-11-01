import secrets
import string


CHARACTER_TYPES = {
    "uppercase": string.ascii_uppercase,
    "lowercase": string.ascii_lowercase,
    "numbers": string.digits,
    "symbols": "!@#$%^&*()-_=+[]{}?",
}


def read_length():
    while True:
        raw_value = input("Password length (minimum 8): ").strip()

        try:
            length = int(raw_value)
        except ValueError:
            print("Enter a whole number for the password length.")
            continue

        if length < 8:
            print("The password must be at least 8 characters long.")
            continue

        if length > 256:
            print("The password length cannot exceed 256 characters.")
            continue

        return length


def ask_yes_no(label):
    while True:
        answer = input(f"Include {label}? (y/n): ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Please answer y or n.")


def choose_character_types():
    while True:
        selected = []

        for name, characters in CHARACTER_TYPES.items():
            if ask_yes_no(name):
                selected.append(characters)

        if len(selected) >= 2:
            return selected

        print("Choose at least two character types.")


def generate_password(length, selected_types):
    password_characters = [
        secrets.choice(characters) for characters in selected_types
    ]

    all_allowed_characters = "".join(selected_types)

    while len(password_characters) < length:
        password_characters.append(secrets.choice(all_allowed_characters))

    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)


def main():
    print("Random Password Generator")

    while True:
        length = read_length()
        selected_types = choose_character_types()
        password = generate_password(length, selected_types)

        print(f"\nGenerated password: {password}")

        while True:
            again = input(
                "Generate another password? (y/n): "
            ).strip().lower()

            if again in ("y", "yes"):
                break

            if again in ("n", "no"):
                print("Done. Keep your password private.")
                return

            print("Please answer y or n.")


if __name__ == "__main__":
    main()
