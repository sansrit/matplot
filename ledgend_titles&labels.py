# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:35:11 2020

@author: Admin
"""

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,8,6]

x2 = [1,2,3]
y2 = [10,13,15]

plt.plot(x, y, label='kathmandu')
plt.plot(x2, y2, label='sindhupalchwok')

plt.xlabel('Dates and time ')
plt.ylabel('Numbers')
plt.title('Corona virus count \n NEPAL')

plt.legend()


plt.show()