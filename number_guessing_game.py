import random
random_num=random.randint(1,100)
lives=3
while lives>0:
    try:
            num=int(input("enter your guess:- "))
            if num==random_num:
                print("Congratulations! You guessed it right") 
                break
            lives-=1
            if lives==1:
                 print("This is your last chance")
            elif lives==0:
                 print(f"you lost it The correct number was {random_num}")  
            elif abs(num-random_num)<=5:
                print("You are close")        
            else:
                print("far off") 
                print(f"You have {lives} lives left")       
                 
    except ValueError:
        print("Invalid input! Please enter a number")


       
     

