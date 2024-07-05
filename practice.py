 #_______________________________________________1- کیلومتر به متر
 
kilo_metr = float(input("Chand KiloMetr ? "))
print(kilo_metr ," KiloMetr Barabar Ast Ba " , kilo_metr * 1000 ," Metr")


 #_______________________________________________2- سانتی گراد به فارنهایت


degree_c = int(input("degree_c: "))
print(f"{degree_c}C = {int(degree_c * 33.8)}F ")


#_______________________________________________3- اعداد اول از عدد ورودی تا صفر 

num = int(input("Num : "))

for j in range(2, num):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        print(j)

#_______________________________________________4- شبیه سازی تاس

import random 

num = random.randint(1,6)

print(f"\n\nNumber: {num}\n\n")


#_______________________________________________5- حدس عدد بین 1000 با دو کاربر و 20 موقعیت و فرصت

op = 20

in_num = int(input("Enter Number In Range 1000: "))

if in_num <= 1000 and in_num >= 0:
    
    for i in range(1, 20):
        
        guess = int(input("enter you guess between 1000 to 0: "))
        
        if guess == in_num:
            print("Win!")
            break
        
        elif guess != in_num:
            op -= 1
            print(f"You Have {op} More opurtiunity!")    

        elif op == 0:
            print("You Lose!")
            break
            
else:
    print("Enter In This Range!")

#____________________________________________6- ساخت رمز ایمن

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


#____________________________________________7- ماشین حساب


answer = 0


while True:
    
    if answer == 0:
        num1 = int(input("Enter A Number: "))
        
    func = int(input("1.Jam - 2.Tafrigh - 3.Zarb - 4.Taghsim - 5.Javab: "))
    
    if func == 5 and answer == 0:
        print(num1)
        break 
    
    elif func == 5 and answer != 0:    
        print(answer)
        break
    
        
    else:
        num2 = int(input(f"number two to do func on num1: "))
        
        if func == 1 and answer != 0:
            answer += int(num2)
        
        elif  func == 2 and answer != 0:
            answer -= int(num2)    
            
        elif  func == 3 and answer != 0:
            answer *= int(num2)      
            
        elif  func == 4 and answer != 0:
            answer //= int(num2)
            
        
        if func == 1 and answer == 0:
            answer = int(num1) + int(num2)
        
        elif  func == 2 and answer == 0:
            answer = int(num1) - int(num2)    
            
        elif  func == 3 and answer == 0:
            answer = int(num1) * int(num2)      
            
        elif  func == 4 and answer == 0:
            answer = int(num1) // int(num2)
            
            
                                  