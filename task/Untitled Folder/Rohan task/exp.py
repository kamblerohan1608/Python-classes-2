# main = ["--","Rohan","Kamble","25","rohan@gmail.com","rohan","--","vaibhav","kamble","24","vaibhav@gmail.com","vaibhav"]

# main = " ".join(main)
# print(main)
# print(type(main))
# main = main.split("--")
# print(main)
# main = [[i] for i in main]
# print(main)



# b = ["Rohan","Kamble","25","rohan@gmail.com","rohan"]
# a = ["first_name","last_name","age","email","password"]

# d= {a[i]:b[i] for i in range(len(a))}
# print(d)

# mail1 = input("Enter the Email : ")
# pass1 = input("Enter the password : ")

# if d["email"] == mail1 and d["password"] == pass1:
#     wel=1
#     print("you have loged in")
# else:
#     print("invalid email or password")



ls = [1,2,3,4,5,6,78,9]
c=ls.index(78)-4
d=f'welcome {c}'
print(d)
