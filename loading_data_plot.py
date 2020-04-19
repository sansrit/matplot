

import matplotlib.pyplot as plt
import numpy as np


'''import csv

x = []
y = []

with open('ktm.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter =',')
    for row in plots:
        x.append(int(row[0]))
        y.append((int(row[1]))
        
        
plt.plot(x, y, label = 'test')
'''

x , y = np.loadtxt('ktm.txt', delimiter = ',' ,unpack = True)

plt.plot(x, y, label = 'test',color = 'r', linewidth = 2)
plt.xlabel('dates')
plt.ylabel('numbers')
plt.title('covid 19 \n status in nepal')
plt.legend()
plt.show()


