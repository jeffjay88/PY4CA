# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:51:19 2019

@author: HP
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#### Use sample data which is available on the github account.
data=sp.genfromtxt('Atmospheric_data.ftr',skip_header=1)
altitude=data[:,1]      #altitude  (column 2)
pressure=data[:,2]      #atmospheric pressure (column 3)
u=data[:,8]             #zonal winds (column 9)


#plt.plot(u,altitude); plt.axvline(x=0)
plt.plot(u,pressure); plt.axvline(x=0); plt.ylim(1000,0)

#plt.axvline is for plotting a vertical line 
#plt.axhline is for plotting a horizontal line 