import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password_chars = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password_chars += random.choices(all_characters, k=length - 4)
    
    random.shuffle(password_chars)
    
    password = ''.join(password_chars)
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 8, 12, 16): "))
            if length < 4:
                print("Password length must be at least 4 to include all categories.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()