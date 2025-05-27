print("----Welcome To Contact Book----")
contacts=[]
while True:
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    user_input=int(input("Enter your choice:- "))


    if user_input==1:
        contact_name=input("Enter name:- ")
        contact_num=int(input("Enter Phone number:- "))
        contacts.append((contact_name,contact_num))
        print("Contact added successfully!\n")


    elif user_input==2:
        if not contacts:
            print("No contacts found\n")
        else:
            print("Here are your contacts\n") 
            for index,contact in enumerate(contacts,start=1):
                print(f"{index}. Name:- {contact[0]}\n Phone number:- {contact[1]}")  


    elif user_input==3:
        name_search=input("Enter the name to search:- ").lower() 
        for contact in contacts:
            if contact[0]==name_search:
                print("contact found")
                print(f"Name:- {contact[0]}\nPhone number:- {contact[1]}") 
                break
        else:
            print("Contact not found")    


    elif user_input==4:
        delete_contact=input("Enter the name of the contact to delete:- ")  
        for contact in contacts:
            if delete_contact==contact[0]:
                contacts.remove(contact) 
                print("Contact deleted successfully\n")  
                break        
            else :
                print("Contact not found\n")

    elif user_input==5:
        print("Exiting Contact Book,Goodbye!")

                
    else:
        print("Please enter a valid number\n")
            


    

