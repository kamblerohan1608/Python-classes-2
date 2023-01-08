def sign_up():
        
    with open("test.txt","a") as file:
        first_name = input("Enter your first name : ")
        last_name = input("Enter your last name : ")
        age = input("Enter your age : ")
        mailid = input("Enter the mail : ")
        password = input("Enter the password : ")
        data = mailid + password
        all_data = f"{first_name}\n{last_name}\n{age}\n{data}\n"
        file.write(all_data)
        file.write("\n")
        print("signed up successfully...\nYou can log in now...")



def log_in():
    
    with open("test.txt","r") as file:
        data = file.readlines()
    new_data = []

    for i in data:
        i = i.replace("\n","")
        new_data.append(i)
        
    mailid1 = input("Enter the mail : ")
    password1 = input("Enter the password : ")

    mp = mailid1+password1

    if mp in new_data:
        global wel
        wel=1
        print("\nYou have successfully loged in...")
    else:
        print("\nIncorrect username or password...Try again")

def main():
    print('''
    **************** Welcome to the Application ********************

    Press 1  : for sign up
    Press 2  : for log in
    press 3  : to Exit''')

main()
print()
while True:
    ch = int(input("Enter your choice : "))
    if ch==1:
        sign_up()
        main()
    elif ch== 2:
        wel = 0
        log_in()
        if wel == 1:
            print("\n\nYou have entered into the application.\n\nEnjoy your Application\n\n")   
            break
        else:
            main()
            print()
    elif ch ==3 :

        print("\n------ Thank You...Visit Again -------\n")
        break
    else:
        print("******Invalid Input...Try Again******")







