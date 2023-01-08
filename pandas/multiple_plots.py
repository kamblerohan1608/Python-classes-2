
# Miltiple plots

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
min_temp = [25,30,35,26,24,37,32]
avg_temp = [30,35,42,32,31,40,39]
max_temp = [35,40,45,42,42,43,44]
plt.xlabel('Days')
plt.ylabel('Temprature')
plt.plot(days,min_temp,color = 'blue',marker = "*",label = 'minimum temprature' )
plt.plot(days,avg_temp,color = 'yellow',marker = "<",label = 'average temprature' )
plt.plot(days,max_temp,color = 'red',marker = "o",label = 'maximum temprature' )
plt.legend()
plt.show()
