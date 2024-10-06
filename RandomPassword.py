import random
import string
def password_generator(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password = random.choice(string.ascii_letters) + ''.join(random.choice(characters) for i in range(length - 1)) 
    return password
print(password_generator(6))
