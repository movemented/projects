import random
import string

print("Hello, Welcome to the Best Password Generator")

length = int(input('How many characters do you want in your password: '))                      

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

generator = random.sample(all,length)

password = "".join(generator)

print(password)
