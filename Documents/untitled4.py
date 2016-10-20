# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 07:18:49 2016

@author: Justin
"""
import pandas
import matplotlib.pyplot as plt

path = '/Users/Justin/Downloads/Lab_3_Data.xls'

file = pandas.read_excel(path, sheetname = 'Small')

filtered_voltage_small = file['small fishing weight'].iloc[2::2].tolist()
filtered_time_small = file['Unnamed: 1'].iloc[2::2].tolist()

taylor_series_voltage_small = []
for i in range(2, len(filtered_voltage_small)-2):
    taylor_series_voltage_small.append((8*(filtered_voltage_small[i+1]-filtered_voltage_small[i-1])+(filtered_voltage_small[i-2]-filtered_voltage_small[i+2]))/(12*(filtered_time_small[i+1]-filtered_time_small[i])))
    
#plt.plot(filtered_time_small[2:-2], taylor_series_voltage_small)
#plt.show()

big_weight = pandas.read_excel(path, sheetname = 'Big')

fil_vol_big = big_weight['Big fishing weight'].iloc[3::3].tolist()
fil_time_big = big_weight['Unnamed: 1'].iloc[3::3].tolist()

taylor_series_voltage_big = []
for i in range(2, len(fil_vol_big)-2):
    taylor_series_voltage_big.append((8*(fil_vol_big[i+1]-fil_vol_big[i-1])+(fil_vol_big[i-2]-fil_vol_big[i+2]))/(12*(fil_time_big[i+1]-fil_time_big[i])))
    
plt.plot(fil_time_big[2:-2], taylor_series_voltage_big)
plt.show()