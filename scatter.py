# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 06:48:45 2020

@author: Admin
"""

import matplotlib.pyplot as plt

x = [2,4,6,8,10,12,14,16]
y = [5,8,2,15,2,5,22,1]

x2 = [1,3,5,7,9]
y2 = [10,13,15,12,19]

plt.scatter(x, y, label='kathmandu',color='r',s= 100, marker ="*")
plt.plot(x2, y2, label='sindhupalchwok', color = 'c')

plt.xlabel('Dates and time ')
plt.ylabel('Numbers')
plt.title('Corona virus count \n NEPAL')

plt.legend()


plt.show()