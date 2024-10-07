import tkinter as tk
import random
import string
def password_generator(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password = random.choice(string.ascii_letters) + ''.join(random.choice(characters) for i in range(length - 1)) 
    return password

root = tk.Tk()
root.title('Random Password Generator!')
root.geometry("300x300")

label = []

def generate_password():
    if len(label) > 0:
        label[0].destroy()
        label.pop()

    label.append(tk.Label(root, text=password_generator(6)))
    label[0].pack()

button = tk.Button(root, text='Generate Password', command=generate_password)
button.pack()

root.mainloop()
