print("Quiz Time!!")
questions = ["What is the capital of India? ", 
             "What is the chemical symbol water? ", 
             "What is the largest ocean on Earth? ", 
             "How many continents are there in the world? ",
             "What is the national flower of India?  "]
answers=["Delhi","h2O","Pacific Ocean","7","Lotus"]
points=0
for i in range(len(questions)):
    user_answer=input(questions[i])

    
    if user_answer.lower()==answers[i].lower():
        points+=1 
        print("That's correct! You got one point")
    else:
        print(f"oops thats incorrect, The correct answer was {answers[i]}") 
           

print(f"Your score is {points}/{len(answers)}")


