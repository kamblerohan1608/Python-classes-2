import re

# '[]' set (creats a set of sequence of characters)

# txt = "i am studying python and creating programs."
# ptr = r'[a-d]'
# data = re.findall(ptr,txt)
# print(data)




## '.' any character (even space except \n)

# text = 'python is p1234n not inopen or kfvooe' 
# ptr = r'p....n'
# x= re.findall(ptr,text)

# print(x)



# ## '^' starts with


# text = '''hello class\n
# hello all
# done or not
# is it fine
# '''

# ptr = r'^hello'

# x= re.findall(ptr,text)
# print(x)


# ## '$' ends with


# text = "hello planet"

# ptr = r'planet$'

# x= re.findall(ptr,text)
# print(x)



## '*' zero or more occurance

# test = 'helllo'
# test1 = 'heo'
# ptr = r'hel*o'

# x= re.findall(ptr,test)
# print(x)
# x= re.findall(ptr,test1)
# print(x)

# ## '+' one or more

# text = "hello planet. helllo"

# ptr = r'hel+o'

# x= re.findall(ptr,text)
# print(x)



## '?' zero or one occurence

# text = "hello planet helo heoss"

# ptr = r'hel?o'

# x= re.findall(ptr,text)
# print(x)



## {} no of ocurences

# text = "hello planet helllo"

# ptr = r'hel{3}o'

# x= re.findall(ptr,text)
# print(x)


## '|' either or

# text = "hello planet hello world"

# ptr = r'p....t|w...d'

# x= re.findall(ptr,text)
# print(x)



# 1 - if a variable is having any sort of value then by default it is True
# 2 - if a variable is empty or having none value assigned then by default it is False

# a= ''
# if a:
#     print("True")
# else:
#     print("False")

