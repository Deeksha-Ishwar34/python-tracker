odd_numbers=[]
even_numbers=[]
for i in range(4):
    num=int(input("Enter the number:- "))
    
    if num % 2==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
else: 
    print("Invalid Input,Please enter a valid number")
    
print(f"Even_numbers:-{even_numbers}\nOdd_numbers:-{odd_numbers}")  
user_choice=input("Do you wanna check the sum of Even and Odd numbers you entered?(Yes/No)").lower()
if user_choice=="yes":
    print(f"Sum of Even numbes{sum(even_numbers)}\nSum of Odd number {sum(odd_numbers)}")



     


