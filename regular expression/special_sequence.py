
import re

# special sequence

## \A start of a string

# text = "hello planet"

# ptr = r'\Ahe'

# x= re.findall(ptr,text)
# print(x)



## \b takes word


# text = "hello planet3 i am here"

# ptr = r'\bpl.*[0-9]+\b'

# x= re.findall(ptr,text)
# print(x)



## \B takes word


# text = "hello planet3 i am here"

# ptr = r'\Bpl.*[0-9]+\B'

# x= re.findall(ptr,text)
# print(x)


## \d digits only

# text = "15464 65454yufuf @ hu 466"

# ptr = r'\d'

# x= re.findall(ptr,text)
# print(x)



## \D everything except digit


# text = "15464 65454yu.%fuf @ hu 466"

# ptr = r'\D'

# x= re.findall(ptr,text)
# print(x)


## \w 

# text = "15464 65454yu.%fuf @ hu 466"

# ptr = r'\D'

# x= re.findall(ptr,text)
# print(x)


# data = '1234567890 369fg145454 3659745812 fh65djd@546 12345678910'
# ptr = r'[0-9]{10}'
# x = re.findall(ptr,data)
# print(x)


