#_______________________________________________ حدس عدد بین 1000 با دو کاربر و 20 موقعیت و فرصت

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