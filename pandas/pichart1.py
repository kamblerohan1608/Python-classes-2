
import matplotlib.pyplot as plt

values = [2000,3000,5000,6000,1500,2000,500]
exp_label = ['food','shopping','rent','investment','travel','saving','other']

plt.pie(values,labels = exp_label , shadow=True, autopct="%1.1f%%",explode = [0,0,0.5,0,0.3,0,0],radius = 1.2)
plt.savefig("pichart.pdf")
plt.show()