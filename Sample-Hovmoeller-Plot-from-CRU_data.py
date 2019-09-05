# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:44:17 2019

@author: HP
"""

### Importing Packages to be used
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib import cm
%matplotlib inline

var='tmp'
nc_f = 'cru_ts4.02.1901.2017.'+var+'.dat.nc'  # Your filename
DS = xr.open_dataset(nc_f)
da = DS.tmp
lons=DS.lon
lats=DS.lat
timer=DS.time

data=da.values  ###For collecting only the parameter values without other metadata


### Transforming data into Monthly Stacks
month_out=[]
for i in range(12):
    try:
        first_out=[]
        for j in np.arange(np.shape(data)[0]):
            if (j%12==i):
                first_out.append(data[j,:,:])
    except:
        pass
    month_out.append(first_out)


    
###Line Plot Generation    
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
col=['r','b','g','y','m','c','grey','k','yellow','b','g','r']
plt.figure(figsize=(7,7))
plt.subplot(111)
for i in range(12):
    plt.plot(np.nanmean(month_out[i],axis=(0,2)),lats.values,label=months[i], color=col[i])
plt.ylim(-90,90)
plt.legend(loc=0, ncol=3)
plt.xlabel(r'Temperature Climatology [$^o$C]')
plt.ylabel('Latitude')
plt.grid(True)
plt.title('Zonal Temperature Climatology (1901-2017)')

plt.savefig('Temperature.png')





### Hovmoller Plot Generation
plt.figure(figsize=(7,7))
plt.subplot(111)
plt.pcolor(np.nanmean(month_out,axis=(1,3)).T,cmap=cm.jet)
plt.yticks(np.arange(0,lats.size,30),lats.values[::30])
plt.xticks(np.arange(12)+0.5,months)
plt.ylim(70,350)
plt.axhline(y=178, color='k')
plt.xlabel('Month', fontsize=15)
plt.ylabel('Latitude', fontsize=15)


plt.savefig('Hovmoller.png')