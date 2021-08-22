import os
import pandas as pd
# generate random integer values
#from random import seed
from random import randint, choice
#from random import choice


# ---------- CHANGES: Indexes can't be chose more than once to avoid eating the same thing twice during the week
# ---------- CHANGES: Add attribute to make menu more equilibrated 
def chooseDish(str):
    subset_df = xl_file[(xl_file['Day'] == str) | (xl_file['Day']=='Any')]
    index = randint(0, len(subset_df))
    dish1 = subset_df['Dish'][index]
    if subset_df['Type'][index] == 'Primo':
        side_dish = subset_df[subset_df['Type']=='Contorno']
        dish2 = choice(list(side_dish['Dish']))
        final_dish = dish1+' & '+dish2
        index_list = [index, subset_df.index]
    elif subset_df['Type'][index] == 'Secondo':
        side_dish = subset_df[subset_df['Type']=='Contorno']
        dish2 = choice(list(side_dish['Dish']))
        final_dish = dish1+' & '+dish2
    elif subset_df['Type'][index] == 'Contorno':
        side_dish = subset_df[subset_df['Type']=='Secondo']
        dish2 = choice(list(side_dish['Dish']))
        final_dish = dish1+' & '+dish2
    else:
        final_dish = dish1
    #index_list = 
    return final_dish


xl_file = pd.read_excel('/Users/mr2814/Desktop/menu_settimanale.xlsx')

week = ['Lunedi','Martedi','Mercoledi','Giovedi','Venerdi','Sabato','Domenica']

# generate some integers
for l in range(7):
    day = week[l]
    if day == 'Lunedi' or day == 'Martedi' or day == 'Mercoledi' or day == 'Giovedi' or day == 'Venerdi':
        dinner = chooseDish(day)
        print(day+'\nCena: '+dinner)
    else:
        lunch = chooseDish(day)
        dinner = chooseDish(day)
        print(day+'\nPranzo: '+lunch+'\nCena: '+dinner)





