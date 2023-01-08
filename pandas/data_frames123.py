import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # converting dictionary to excel data

# data = {"days":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"temp" : ["31","32","30","28","35","39","40"],"Wind speed":["10","11","12","10","11","12","15"],"Event" : ["Sunny","Snow","Rain","cloudy","Sunny","Sunny","cloudy"]}

# print(data)

# df = pd.DataFrame(data)

# print(df)

# # converting to cvs file

# df.to_csv("data.csv",index= False)

# # shape 

# print(df.shape)



# extract data from csv file : 
 

df = pd.read_csv("data.csv")
# print(df)



# row operations



# First rows
# print(df.head())          # five default
# print(df.head(3))

# # last rows
# print(df.tail())        # five default
# print(df.tail(3))

# print(df[2:6])


# # Column operations



# col = df[["temp","Event"]]
# print(col)
# print(type(col))      # Data Frame

# col = df["temp"]
# print(col)
# print(type(col))      # Series


# # extract multiple column values 

# col = df[["temp","Event"]].values
# print(col)
# print(type(col))          # ndarray


# # extract single value 

# col = df["temp"].values
# print(col)
# print(type(col))



# # extracting inbetween data (iloc)

# col = df.iloc[1:5,1:3]
# print(col)               # dataframe

# col = df.iloc[1:5,1:3].values
# print(col)              # array




# dataframe queries :



# # max value of a column

# a=df["temp"].max()
# print(a)

# # min value of cloumn 

# b = df["temp"].min()
# print(b)

# # average value or mean

# c = df["temp"].mean()
# print(c)



# # Condition queries
 
# # data of temprature more than 30

# d = df[df["temp"]>30]
# print(d)

# # data when event is sunny

# e =df[df["Event"]=="Sunny"]
# print(e)

X = df["days"].values
Y = df["temp"].values
plt.plot(X,Y,color = "orange",marker = "o",markersize = 5,linestyle = "-.", alpha = 0 )
plt.show()



