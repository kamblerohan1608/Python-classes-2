

# with open("mehul123.txt","a") as file :
#     name = input("Enter your name : ")
#     salary = input("Enter your salary : ")
#     location = input("Enter your location : ")
#     data = (f"{name},{salary},{location}")
#     file.write(data)

with open("mehul123.txt","r") as file :
    data = file.readlines()
    for i in data:
        i=i.split(',')
        print(i)
    name = i[0]
    print(name)
    salary = 20000
    location = i[2]
    data = (f"{name},{salary},{location}")

with open("mehul123.txt","w") as file:
    file.write(data)