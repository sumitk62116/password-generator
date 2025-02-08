import random

def generate_password(length=12):
    # Define the character sets
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?'
    
    # Combine all character sets
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string and return
    return ''.join(password)

# Example usage
if _name_ == "_main_":
    password_length = 12  # You can change this to your desired length
    password = generate_password(length=password_length)
    print("Generated Password:", password)