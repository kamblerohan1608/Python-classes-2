
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
