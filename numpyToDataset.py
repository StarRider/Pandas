# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:55:53 2018

@author: SHALOM ALEXANDER
"""

import pandas as pd
import numpy as np

#creating dataset using numpy array
arr = np.array([['','Name','Sem'],[1,'sharon',7],[2,'himanshu',1],[3,'shubham',7]])

data = pd.DataFrame(data = arr[1:,1:],index = arr[1:,0],columns = arr[0,1:])

print(data)


#creating dataset without mentioning the row and column
new_arr = np.array([[1,2],[2,5],[9,0]])

new_data = pd.DataFrame(new_arr)

print(new_data)

#creating dataset from dictionary

my_dict = {
            'City':['Delhi','Mumbai','Kashmir'],
            'Country':['India','USA','Egypt'],
            'River':['Krishna','Ganga','Amazon']
        }

dict_data = pd.DataFrame(my_dict)

print(dict_data) 

#creating row index and column index in an automated fashion

blah = np.array([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,0,0],[1,0,1,1,0],[1,0,1,0,1]])
col_index = ['Blah ' + str(i) for i in range(len(blah[0]))]
row_index = [i for i in range(len(blah))]
blah_data = pd.DataFrame(data = blah,index = row_index,columns = col_index)


