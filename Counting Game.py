print("Welcome to the Counting game ;)))))):")
num = 0

while num < 15:
    print("Player 1's Go")
    p1 = int(input("How many numbers: "))  
    
    if p1 == 1: 
        num = num + 1
    elif p1 == 2:
        num = num + 2
    elif p1 == 3:
        num = num + 3
    if num >= 15:
        print("Player 1 reached 15 — Player 1 loses! 😢")
    print("The current number is", num)      
     
    print("Player 2's Go")
    p2 = int(input("How many numbers: "))  
    
    if p2 == 1: 
        num = num + 1
    elif p2 == 2:
        num = num + 2
    elif p2 == 3:
        num = num + 3
    if num >= 15:
        print("Player 2 reached 15 — Player 2 loses! 😢")           

    print("The current number is", num)
 




   






#Player1=int(input("How many numbers?:"))
#if Player1 == 1 :
#    Number=int(input("Pick your first number:"))
#elif Player1 == 2:
#    Number=int(input("Pick your first number:"))
#    Number2=int(input("Pick your Second number:"))
#elif Player1 == 3:
#    Number=int(input("Pick your first number:"))
#    Number2=int(input("Pick your Second number:"))
#    Number3=int(input("Pick Your third number:"))
   