num_of_stu=int(input("Enter number of students:- "))
students_list=[]
unique_cities=set()
for i in range(num_of_stu):
    print(f"Enter the details of student {i+1}")
    name=input("Name:- ")
    age=input("Age:- ")
    marks=int(input("Marks:- "))
    city=input("City:- ")
    reg_no=int(input("Reg no:- "))
    branch=input("Branch:- ")
    students={
        "name":name,
         "age":age,
         "marks":marks,
         "city":city,
         "reg_no":reg_no,
         "branch":branch
    }
    students_list.append(students)
    unique_cities.add(city)

print("----Student Details----")
for student in students_list:
    print(student)

print(unique_cities)           
