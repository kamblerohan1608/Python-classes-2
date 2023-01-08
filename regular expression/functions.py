import random,re

# exp : 

# findall: 

# l = 'rohan@gmail.com , sagar123@gmail.com, kishor567_1@yahoo.in'

# ptr = r'\b[a-zA-Z0-9.*_*-*]+@[a-zA-Z]+\.[a-zA-Z]{2,}'

# x = re.findall(ptr,l)

# print(x)


# Example 2 :

# def check_mail(mail):
#     ptr = r'[a-z0-9\.*_*]+@[a-z]+\.+[a-z\.*]+'
#     x = re.findall(ptr,mail)
#     if x:
#         return x
#     else:
#         return None

# print(check_mail("rohan@gmail.com"))
# print(check_mail("suman123@gmail.com"))
# print(check_mail("raksh_12.3@gmail.com"))
# print(check_mail("rohan@@gmail.com"))

# match:

# l = 'rohan, sagar123@gmail.com, kishor567_1@yahoo.in'

# ptr = r'\b[a-zA-Z0-9.*_*-*]+@[a-zA-Z]+\.[a-zA-Z]{2,}'

# x = re.match(ptr,l)
# print(x.group())
# ptr = r'\b[a-zA-z]+\b'
# name_1 = 'rohan'
# x_1 =re.match(ptr,name_1)
# print(x_1.group())

# name = 'rohan123'
# x = re.match(ptr,name)
# print(x.group())


# Example 2 :

# text = "python class"
# ptr = r'p.{4}n'
# x = re.match(ptr,text)
# print(x.group())
# print(x.span())


# search:


# l = 'rohan , sagar123@gmail.com, kishor567_1@yahoo.in'

# ptr = r'\b[a-zA-Z0-9.*_*-*]+@[a-zA-Z]+\.[a-zA-Z]{2,}'

# x = re.search(ptr,l)
# print(x.group())
# # print(x)


# Example 2 :

# text = "an apple or a class of python"
# ptr = r'p.{4}n'
# x = re.search(ptr,text)
# print(x.group())
# print(x.span())


# sub:

# l = 'rohan@gmail.com , sagar123@gmail.com, kishor567_1@yahoo.in'

# ptr = r'\b[a-zA-Z0-9.*_*-*]+@[a-zA-Z]+\.[a-zA-Z]{2,}'

# x = re.sub(ptr,'00',l)

# print(x)


# Example 2 : 

# ptr = r'\d'
# text = "123 Rohan 256hello there 586"
# x = re.sub(ptr,'',text)
# print(x)




ptr = r'\b[a-zA-z]+\b'
name = 'Rohan'
x_1 =re.match(ptr,name)
print(x_1.group())

name_1 = 'rohan123'
x = re.match(ptr,name_1)
print(x.group())