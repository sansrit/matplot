# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:04:27 2020

@author: Admin
"""


import matplotlib.pyplot as plt

Dates = [2,4,6,8,10,12]

ktm= [5,8,2,15,2,5]
bkt = [1,3,5,7,9,12]
sindhu = [10,13,15,12,19,9]

plt.stackplot(Dates, ktm,bkt,sindhu,colors=['m','c','r','k'])
plt.plot([],[], color = 'm', label = 'kathmandu', linewidth = 5)
plt.plot([],[], color = 'c', label = 'bhaktapur', linewidth = 5)
plt.plot([],[], color = 'r', label = 'sindhupalchowk',linewidth = 5)


#plt.plot(Dates, sindhu, label='sindhupalchwok', color = 'c')
#plt.plot(Dates, ktm, label='kathmandu',color='b')
#plt.plot(Dates, bkt, label='bhaktapur',color='r')

plt.xlabel('Dates and time ')
plt.ylabel('Numbers')
plt.title('Corona virus count \n NEPAL')

plt.legend()


plt.show()