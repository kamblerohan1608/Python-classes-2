# duck typing

# if it looks like a duck, work like a duck and sounds like a duck it is a duck

# class india:
#     def capital(self):
#         print("Capital of India is Delhi")
#     def language(self):
#         print("Language spoken is Hindi")
    
# class USA:
#     def capital(self):
#         print("Capital of USA is Washington DC")
#     def language(self):
#         print("Language spoken is English")

# A=india()
# B=USA()

# for obj in (A,B):    
#     obj.capital()
#     obj.language()

class india:
    def capital(self):
        print("Capital of India is Delhi")
    def language(self):
        print("Language spoken is Hindi")
    
class USA:
    def capital(self):
        print("Capital of USA is Washington DC")
    def language(self):
        print("Language spoken is English")

A=india()
B=USA()

def main(obj):
    obj.capital()
    obj.language()

main(A)
main(B)

