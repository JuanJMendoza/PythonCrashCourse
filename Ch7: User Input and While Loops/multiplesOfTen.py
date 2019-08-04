num = input("Choose a number, any number. ")
num = int(num)

if(num % 10 == 0):
    print(f"{num}, the number you chose, is a multiple of 10!")
else:
    print(f"{num}, the number you chose, is not a multiple of 10!")