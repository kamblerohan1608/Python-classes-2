
import matplotlib.pyplot as plt
import numpy as np

comp = ['Facebook','Amazon','Flipcart','google']

revenu = [100000,200000,300000,400000]
profit = [50000,100000,250000,150000]
x_pos = np.arange(len(comp))
# print(x_pos)
plt.bar(x_pos-0.2,revenu,width = 0.4,label = 'revenu')
plt.bar(x_pos+0.2,profit,width = 0.4,label = 'profit')
plt.xticks(x_pos,comp)

plt.legend()
plt.grid()
plt.savefig("bar_graph.jpg")
plt.show()
