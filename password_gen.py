import random
import secrets
import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
all_characters = lowercase + uppercase + digits + symbols

while True:

    try:
        length = int(input("How many long characters should the password be (minimum 6)? "))
        if length < 6:
            print("Password length must be at least 6 characters. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


password_chars = [
    secrets.choice(lowercase),
    secrets.choice(uppercase),
    secrets.choice(digits),
    secrets.choice(symbols)
]


# 4. Loop through the range of the length of the password
for i in range(length - 4):
    password_chars.append(secrets.choice(all_characters))

secrets.SystemRandom().shuffle(password_chars)

password = ''.join(password_chars)
    
print("Your Generated Password is: ", password)