import config_1

login_flag = False

def log_in():
    global login_flag
    with open("test2.txt","r") as file:
        data = file.readlines()               # file data
    global main
    main = []
    for i in data:
        i = i.replace("\n","")
        main.append(i)                        # removing \n
    main = " ".join(main)                     # to form a string
    main = main.split("--")                   # forming saperate lists of each user info
    main.pop()                                # deleting last empty list 

    new_main =[]
    for i in main:
        i=i.split()
        new_main.append(i)                    # turning string into elements of lists

    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    for i in new_main:
        l1.append(i[0])
        l2.append(i[1])
        l3.append(i[2])
        l4.append(i[3])
        l5.append(i[4])
    l = [l1,l2,l3,l4,l5]                      # list of values to be set for dictionary
    all_info = {}
    keys = ["first_name","last_name","age","id","password"]    # keys of the list
    for i in range (len(keys)):
        all_info[keys[i]] = l[i]                                      # forming dictionary
    #print(all_info)

    while True:    
        email_1 = input("Enter the mail : ")
        if "@" in email_1 and "." in email_1:
            break
        elif "@" not in email_1:
            print("'@' is missing in the mail Id. Try again..")
        elif "." not in email_1:
            print("'.' is missing in mail Id. Try again..")
    while True:
        password1 = input("Enter the password : ")
        if len(password1) > 4:
            break
        else:
            print("Password must be more than 4 characters. Try again..")

    if email_1 in all_info["id"]:
        indx_list = all_info["id"]
        indx_id = indx_list.index(email_1)
        # print(indx_id)
        if all_info["password"][indx_id] == password1 :
            name = all_info["first_name"][indx_id]
            login_flag = True
            print(f'''  
                        -------------------------------------------------------
                        |       Welcome to the application {name.capitalize()} ...          |
                        -------------------------------------------------------
                        
                        ''')
            config_1.wel = 2
        else:
            print("\nInvalid id or password.\nTry Again...\n")  
    else:
        print("\nInvalid id or password.\nTry Again...\n")