#____________________________________________ ساخت رمز ایمن

import random

characters = [
    
    "a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "1","2","3","4","5","6","7","8","9",
    "!","@","#","$","%","^","&","*","(",")","[","]","{","}",
]

while True:
    
    length = int(input("Enter Length of safe password to create: "))
    
    password = []
    
    if length >= 5 and length <= 20:
        
        for i in range(length):
            rand_char =  random.randint(characters.index(characters[0]), len(characters) - 1)
            password.append(characters[rand_char])
            
            if i == length - 1:
                print(f"\nyour safe password: '{"".join(password)}'\n")
            continue
    
    else:
        print("Length Must be upper than 5 and must be smaller than 20!!") 