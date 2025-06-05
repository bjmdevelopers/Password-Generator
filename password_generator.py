import random
import string
import os

def generate_password(length, char_sets):
    """Generate a password with at least one character from each selected set"""
    password = [random.choice(chars) for chars in char_sets]
    all_chars = ''.join(char_sets)
    password.extend(random.choices(all_chars, k=length - len(password)))
    random.shuffle(password)
    return ''.join(password)

def get_valid_integer(prompt, default, min_val=None, max_val=None):
    """Get a valid integer input with optional min/max limits"""
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            return default
        try:
            value = int(user_input)
            if min_val is not None and value < min_val:
                print(f"⚠️ Must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"⚠️ Must be no more than {max_val}.")
                continue
            return value
        except ValueError:
            print("⚠️ Please enter a valid number.")

def save_to_file(passwords, file_name="/Download/generated_passwords.txt"):
    try:
        with open(file_name, "a") as f:
            f.write("\n".join(passwords) + "\n")
        print(f"\n✅ Saved to: {file_name}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def main():
    print("\n╭───────────────────────────────╮")
    print("│      PASSWORD GENERATOR      │")
    print("╰───────────────────────────────╯")

    while True:
        length = get_valid_integer("\nPassword length (default 16): ", 16, min_val=4, max_val=256)
        
        char_sets = []
        if input("Include uppercase letters (A-Z)? [Y/n]: ").lower() != 'n':
            char_sets.append(string.ascii_uppercase)
        if input("Include lowercase letters (a-z)? [Y/n]: ").lower() != 'n':
            char_sets.append(string.ascii_lowercase)
        if input("Include numbers (0-9)? [Y/n]: ").lower() != 'n':
            char_sets.append(string.digits)
        if input("Include symbols (!@#$...)? [Y/n]: ").lower() != 'n':
            char_sets.append(string.punctuation)

        if not char_sets:
            print("⚠️ You must select at least one character type!")
            continue

        if length < len(char_sets):
            print(f"⚠️ Length must be at least {len(char_sets)} to include all selected types.")
            continue

        count = get_valid_integer("\nHow many passwords to generate (default 1): ", 1, min_val=1)

        passwords = [generate_password(length, char_sets) for _ in range(count)]

        print("\n╭───────────────────────────────╮")
        for pwd in passwords:
            print("│", pwd)
        print("╰───────────────────────────────╯")

        # Ask to save to .txt file
        if input("\nSave passwords to .txt file and download? [Y/n]: ").lower() != 'n':
            save_to_file(passwords)

        if input("\nGenerate more? [Y/n]: ").lower() == 'n':
            break

if __name__ == "__main__":
    main()