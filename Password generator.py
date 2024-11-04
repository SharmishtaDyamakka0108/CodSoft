#Password generator program (updated one)
import secrets
import string

class Password:
    def __init__(self, letters, special_characters, digits, password_len):
        self.letters = letters
        self.special_characters = special_characters
        self.digits = digits
        self.password_len = password_len

    def generate_password(self):
        # Combine all character types
        selection_list = self.letters + self.special_characters + self.digits
        password = ''

        # Generate the password
        for i in range(self.password_len):
            password += secrets.choice(selection_list)

        return password

    def display(self):
        password = self.generate_password()
        print(f"My own Password: {password}")

# Define character sets
letters = string.ascii_letters  # Includes both lowercase and uppercase letters
special_characters = '@*#%&$!/^'
digits = string.digits  # '0123456789'

# Set password length
password_len = 15

# Create an instance of Password
P1 = Password(letters, special_characters, digits, password_len)
P1.display()
