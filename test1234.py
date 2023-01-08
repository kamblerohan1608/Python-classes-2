
#if statement
'''
obtain = int(input("Enter the obtained marks : "))
total = int(input("Enter the total marks : "))
if (total > obtain):
    per=obtain/total*100
    print("Your percentages are",per)
elif (obtain > total):
    per = total/obtain*100
    print("Your percentages are",per)
print("Program finished")

 #swap method

obtain = int(input("Enter the obtained marks : "))
total = int(input("Enter the total marks : "))
if (total < obtain):
    total,obtain=obtain,total
per=obtain/total*100
print("Your percentages are",per)
'''

