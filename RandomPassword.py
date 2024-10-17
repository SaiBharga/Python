# from jinja2 import Template
from flask import Flask, render_template, request
import random
import string
 
app = Flask(__name__)
 
def generate_password(length):
    # special_chars="$@#"
    # characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + special_chars
    # password = ''.join(random.choice(characters) for _ in range(length))
    # return password
    lowercase = string.ascii_lowercase
    uppercase =string.ascii_uppercase
    digits = string.digits
    special_chars = "$@#"
    all_chars = lowercase+uppercase+digits+special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
     # Fill remaining length with random characters
    for _ in range(length-4):
        password.append(random.choice(all_chars))
 
    # Shuffle list to avoid first characters always being in same character set
    random.shuffle(password)
 
    return "".join(password)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
        return render_template('index.html', password=password)
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)     