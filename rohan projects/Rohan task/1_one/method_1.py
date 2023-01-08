def sign_up():
    with open("test.txt","a") as file:
        first_name = input("Enter your first name : ")
        last_name = input("Enter your last name : ")
        age = input("Enter your age : ")
        while True:    
            mailid = input("Enter the mail : ")
            if "@" in mailid and "." in mailid:
                break
            elif "@" not in mailid:
                print("'@' is missing in the mail Id. Try again..")
            elif "." not in mailid:
                print("'.' is missing in mail Id. Try again..")
        while True:
            password = input("Enter the password : ")
            if len(password) > 4:
                break
            else:
                print("Password must be more than 4 characters. Try again..")
        data = mailid + password
        file.write(f"{first_name}\n{last_name}\n{age}\n{data}")
        file.write("\n\n")
    print("\nSigned Up Successfully....\nYou can log in now....")

def log_in():
    with open("test.txt","r") as file:
        data = file.readlines()
    global new_data
    new_data = []
    for i in data:
        i = i.replace("\n","")
        new_data.append(i)
    while True:    
        mailid1 = input("Enter the mail : ")
        if "@" in mailid1 and "." in mailid1:
            break
        elif "@" not in mailid1:
            print("'@' is missing in the mail Id. Try again..")
        elif "." not in mailid1:
            print("'.' is missing in mail Id. Try again..")
    while True:
        password1 = input("Enter the password : ")
        if len(password1) > 4:
            break
        else:
            print("Password must be more than 4 characters. Try again..")
    global mp
    mp = mailid1+password1

    if mp in new_data:
        global wel
        wel=1
        print("\nYou have successfully loged in...")
    else:
        print("\nIncorrect username or password...Try again")


def main():
    print('''
    **************** Welcome to the Application 1 ********************

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
        print()
    elif ch== 2:
        wel = 0
        log_in()
        if wel == 1:
            indx = new_data.index(mp)
            print(f"\n\nWelcome {new_data[indx-3]} {new_data[indx-2]},\n\n")
            break
        else:
            main()
            print()
    elif ch ==3 :

        print("\n------ Thank You...Visit Again -------\n")
        break
    else:
        print("******Invalid Input...Try Again******")
