# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:59:44 2018

@author: SHALOM ALEXANDER
"""
import pandas as pd

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

print(df)

# 1st row selection
first_row = df.iloc[0]
print(first_row)

# 1st row selection next way
first_row = df.iloc[0,:]
print(first_row)

# 1st column
first_col = df.iloc[:,0]  
print(first_col)

# 1st column next way using loc
first_col = df.loc[:,'first_name'] #unfortunately this way isn't possible in iloc[]  
print(first_col)
'''
Why iloc doesn't work like that?
Well, iloc works on positions on your index.
Where as loc works on labels, therefore when a label is mentioned it
goes out and looks out for the element under that label.

There is one more function like iloc and loc it's 'ix[]'
its somewhat the hybrid form of both. When your index is integer based
it works on positions but when its not integer based it works on labels like 
'loc'.
'''

# (1,1) element
element = df.iloc[0,0]
print(element)

# (1,1) element another way
element = df.iloc[0][0]
print(element)

# (1,1) element another way
element = df.iloc[0]['first_name'] #first_name is the 1st column
print(element)

#similar functions like iloc is 'iat[]','loc[]','at[]','ix[]'



