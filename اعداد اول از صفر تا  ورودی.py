#_______________________________________________ اعداد اول از عدد ورودی تا صفر 

num = int(input("Num : "))

for j in range(2, num):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        print(j)