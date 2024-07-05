#____________________________________________ ماشین حساب ساده 


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