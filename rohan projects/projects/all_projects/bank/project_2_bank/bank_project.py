
# Bank Application 

import os

class Main_app:
    def __init__(self):
        try:
            os.mkdir("bank_data")
        except:
            pass
    def check_bal(self,email):
        with open(fr"bank_data/{email}.txt","r") as file:
            data = file.readlines()
        data = data[-1]
        data = data.replace("\n",'')
        #print(data)
        ind = data.index(':')
        #print(ind)
        data =int(data[ind+2:])
        #print(data)
        print(f"\nThe Current Balance Of Account Is : {data}\n")

    def deposite(self,email,depo_amount):
        with open(fr"bank_data/{email}.txt","r") as file:
            data = file.readlines()
        data = data[-1]
        data = data.replace("\n",'')
        #print(data)
        ind = data.index(':')
        #print(ind)
        data =int(data[ind+2:])
        data = data + depo_amount
        with open(fr"bank_data/{email}.txt","a") as file:
            print((f"\nThe Amount Deposited To Account : {depo_amount}\n"))
            file.write(f"The Amount deposited : {depo_amount}\n")
            file.write(f"Balance : {data}\n")

    def withdrawal(self,email,withdraw_amount):
        with open(fr"bank_data/{email}.txt","r") as file:
            data = file.readlines()
        data = data[-1]
        data = data.replace("\n",'')
        #print(data)
        ind = data.index(':')
        #print(ind)
        data =int(data[ind+2:])
        if withdraw_amount > data:
            print("\n********* Insuficient Balance for withdrawal *********\n")
        else:
            data = data - withdraw_amount
            with open(fr"bank_data/{email}.txt","a") as file:
                print((f"\nThe Amount Deducted from Account : {withdraw_amount}\n"))
                file.write(f"The Amount Withdraw : {withdraw_amount}\n")
                file.write(f"Balance : {data}\n")

    def Emi(self,principal,period):
        print(r"Rate of intrest will be 18% for personal loan.")
        rate = 18/12/100
        emi_amount = (principal*rate) * ((1+rate)**period)/(((1+rate)**period)-1)
        emi_amount = round(emi_amount,3)
        print(f"EMI Amount per Month Will Be {emi_amount}")
    
    def history(self,email):
        with open(fr"bank_data/{email}.txt","r") as file:
            data = file.read()
            ind = data.index("The account for")
            print(data[ind:])
            

class Create_Login_account(Main_app):
    def __init__(self):        
        try:
            os.mkdir("bank_data")
        except:
            pass
        self.open_flag = False
        self.log_in_flag = False
        super().__init__()
    def open_account(self,name,age,contact,email,address,amount,password):
        with open(fr"bank_data/{email}.txt","a") as file:
            file.write(f"Name of customer is : {name}\n")
            file.write(f"Age of customer is : {age}\n")
            file.write(f"Contact of customer is : {contact}\n")
            file.write(f"Address of customer is : {address}\n")
            file.write(f"Amount For First Deposite : {amount}\n")
            file.write(f"email of customer is : {email}\n")
            file.write(f"Password is : {password}\n\n")
            print(f"\nThe account for {name} has been created with depositing amount of : {amount}")
            file.write(f"The account for {name} has been created with depositing amount of : {amount}\n")
            self.open_flag = True
        return self.open_flag

    def log_in_account(self,email,password):
        all_files = os.listdir("bank_data")
        all_files_1 = ''.join(all_files)
        if email in all_files_1:
            with open(fr"bank_data/{email}.txt","r") as file:
                data = file.readlines()
                #print(data)
            data = data[6]
            #print(data)
            new_password = data[14:]
            new_password = new_password.replace("\n",'')
            if new_password == password:
                self.log_in_flag = True
        return self.log_in_flag


if __name__=="__main__":

    app = Create_Login_account()
    def front():
        print("******** Welcome To The OneBank Registration ****************\n")
        print("\nPress 1 : Create Account\nPress 2 : Login Account\nPress 3 : Exit Application\n")
    front()
    while True:        
        f_ch = int(input("Enter Your Choice : "))
        if f_ch == 1 :
            name = input("Enter Your Name : ")
            age = input("Enter Your Age : ")
            contact = input("Enter Your Contact Number : ")
            address = input("Enter Your Address : ")
            amount = input("Enter Initial Amount Of Deposite : ")
            email = input("Enter Your Email : ")
            while True:
                password = input("Enter Your Password : ")
                c_password = input("Enter Your Password : ")
                password = password.strip()
                c_password = c_password.strip()
                if len(password) < 6:
                    print("\n******** Password Too Short has to be 6 characters Minimum ********\n")
                elif len(password) > 15 :
                    print("\n******** Password Too long maximum 15 characters allowed ********\n")
                elif password != c_password:
                    print("\n********* Passsword Does not Match**********\n")
                else:
                    break
            name = name.strip()
            age = age.strip()
            contact = contact.strip()
            email = email.strip()
            address = address.strip()
            amount = amount.strip()
            password = password.strip()
            c_password = c_password.strip()

            o_flag = app.open_account(name,age,contact,email,address,amount,password)
            if o_flag == False:
                print("\n******* Something Went Wrong ******\n")
            else:
                print("\n*********** You Can Log In Now ***********\n")
                front()

        elif f_ch == 2 :
            email = input("Enter Your Email id : ")
            password = input("Enter Your Password : ")
            email = email.strip()
            password = password.strip()
            log_f = app.log_in_account(email,password)
            if log_f == False:
                print("\n*********** Incorrect Email Id Or Password *************\n")
                front()
            else:
                def main():
                    print("\n********** Welcome to The OneBank Application ***********\n")
                    print("Press 1 : Check Balance\nPress 2 : Deposite Balance\nPress 3 : Withdraw Amount\nPress 4 : Check Loan EMI\nPress 5 : See Payment History\nPress 6 : Log Out Account")
                main()
                while True:
                    print()
                    m_ch = int(input("Enter Your choice : "))
                    if m_ch == 1:
                        app.check_bal(email)
                        main()
                    elif m_ch == 2:
                        depo_amount = int(input("Enter The Amount To Be Deposited : "))
                        app.deposite(email,depo_amount)
                        main()
                    elif m_ch == 3:
                        withdraw_amount = int(input("Enter The Amount To Withdraw : "))
                        app.withdrawal(email,withdraw_amount)
                        main()
                    elif m_ch == 4:
                        principal = int(input("Enter The Amount of loan : "))
                        period = int(input("Enter The Number of Months : "))
                        app.Emi(principal,period)
                        main()
                    elif m_ch ==5:
                        print("\n*********** All Transactions From Your Account *************\n")
                        app.history(email)
                        main()
                    elif m_ch == 6:
                        print("\n******* logged out of account ********\n")
                        front()
                        break
                    else:
                        print("\n********** Invalid Choice ***********\n")
                        main()
        elif f_ch == 3 :
            print("\n*********** Thank You For Using OneBank Application *****************\n")
            break
        else:
            print("\n************* Invalid Option ****************\n")