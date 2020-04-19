# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:22:55 2020

@author: Admin
"""

import matplotlib.pyplot as plt

Dates = [2,4,6,8,10,12]

ktm= [5,8,2,15,2,5]
bkt = [1,3,5,7,9,12]
sindhu = [10,13,15,12,19,9]


portion = [8,2,1,4]
act = ['gym', 'swimming', 'chess', 'reading']
col = ['c', 'm', 'r', 'k']

plt.pie(portion , labels = act, colors = col, shadow = True, startangle = 90)




plt.title('Corona virus count \n NEPAL')

plt.legend()


plt.show()