# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:43:41 2018

@author: SHALOM ALEXANDER
"""
import pandas as pd
#saving the dataframe to csv
my_dict = {
            'City':['Delhi','Mumbai','Kashmir'],
            'Country':['India','USA','Egypt'],
            'River':['Krishna','Ganga','Amazon']
        }

dict_data = pd.DataFrame(my_dict)

dict_data.to_csv('data.csv')

#loading csv

#with header
new_dict = pd.read_csv('data.csv',names = ['S.No','City','Country','River'])
print(new_dict)

#simply passing
new_dict = pd.read_csv('data.csv')
print(new_dict)

#without header
new_dict = pd.read_csv('data.csv',header = None)
print(new_dict)


