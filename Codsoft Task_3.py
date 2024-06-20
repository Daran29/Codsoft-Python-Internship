import random
import string

num=int(input('Enter the number of Characters: '))

Character_list=(string.ascii_letters+string.digits)*3+string.punctuation

password=[]

for i in range(num):
        new_char=random.choice(Character_list)
        password.append(new_char)
        
print("The random password is " + "".join(password))