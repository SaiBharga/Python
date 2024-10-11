from flask import Flask
import random
import string

def password_generator(length):
    
    lowercase = string.ascii_lowercase
    uppercase =string.ascii_uppercase
    digits = string.digits
    special_chars = "@#$"
    all_chars = lowercase+uppercase+digits+special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
     # Fill remaining length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
 
    # Shuffle list to avoid first characters always being in same character set
    random.shuffle(password)
 
    return "".join(password)

app = Flask(__name__)

@app.route("/")
def main():
    while True:
        length = int(input("Enter password length (10-16): "))
        if 10 <= length <= 16:
            password = password_generator(length)
            print("Generated Password : ", password)
            break
        else:
            print("Password length must be between 10 and 16. Please try again.")
 
if __name__ == '__main__':
    app.run()
