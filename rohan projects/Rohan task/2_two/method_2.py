
def sign_up():
    with open("test2.txt","a") as file:
        first_name = input("Enter your first name : ")
        last_name = input("Enter your last name : ")
        age = input("Enter your age : ")
        while True:    
            id = input("Enter the mail : ")
            if "@" in id and "." in id:
                with open("test2.txt","r") as file1:
                    data = file1.readlines()
                    com_data = []
                    for i in data:
                        i = i.replace("\n","")
                        com_data.append(i)
                if id not in com_data:
                    break
                else:
                    print("Email already exist ... Try another email id...")                        
            elif "@" not in id:
                print("'@' is missing in the mail Id. Try again..")
            elif "." not in id:
                print("'.' is missing in mail Id. Try again..")
        while True:
            password = input("Enter the password : ")
            if len(password) > 4:
                break
            else:
                print("Password must be more than 4 characters. Try again..")
        
        file.write(f"{first_name}\n{last_name}\n{age}\n{id}\n{password}\n")
        file.write("--\n")
    print("\nSigned Up Successfully....\nYou can log in now....")


def log_in():
    with open("test2.txt","r") as file:
        data = file.readlines()
    #print(data)
    global main
    main = []
    for i in data:
        i = i.replace("\n","")
        main.append(i)
    #print(main)
    main = " ".join(main)
    #print(main)
    #print(type(main))
    main = main.split("--")
    #print(main)
    main = [i.split() for i in main]
    #print(main)
    while True:    
        id_1 = input("Enter the mail : ")
        if "@" in id_1 and "." in id_1:
            break
        elif "@" not in id_1:
            print("'@' is missing in the mail Id. Try again..")
        elif "." not in id_1:
            print("'.' is missing in mail Id. Try again..")
    while True:
        password1 = input("Enter the password : ")
        if len(password1) > 4:
            break
        else:
            print("Password must be more than 4 characters. Try again..")

    ind_1 = 0
    list_index1 = 0
    ind_2 = 0
    for i in main:
        for j in i:
            if j == id_1:
                ind_1 = (i.index(j))
                list_index1 = main.index(i)
            elif j == password1 and main.index(i) == list_index1:
                ind_2 = (i.index(j))
                
    if (ind_2 - ind_1 == 1):
        global wel
        wel=1
        print(f"\nWelcome to the application {main[list_index1][ind_1 - 3]} ...")
    else:
        print("\nInvalid id or password.\nTry Again...")    
    
def front():
    print('''
    -------------------- Welcome to the Application 2 ------------------------

    Sign up  :  Press 1
    log in   :  Press 2
    exit     :  Press 3''')
front()
print()
while True:
    ch = int(input("Enter your choice : "))
    if ch==1:
        sign_up()
        front()
        print()
    elif ch== 2:
        wel = 0
        log_in()
        if wel == 1:
            print("\n\n Enjoy your games...\n\n")
            break
        else:
            front()
            print()
    elif ch ==3 :

        print("\n------ Thank You...Visit Again -------\n")
        break
    else:
        print("******Invalid Input...Try Again******")
