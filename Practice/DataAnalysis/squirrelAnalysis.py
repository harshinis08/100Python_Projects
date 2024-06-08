import pandas as pd

df = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240412.csv')

grey_color = df[df['Primary Fur Color'] == 'Gray']
grey_color_count = len(df[df['Primary Fur Color'] == 'Gray'])
print(grey_color_count)

red_color = df[df['Primary Fur Color'] == 'Cinnamon']
red_color_count = len(df[df['Primary Fur Color'] == 'Cinnamon'])
print(red_color_count)

black_color = df[df['Primary Fur Color'] == 'Black']
black_color_count = len(df[df['Primary Fur Color'] == 'Black'])
print(black_color_count)

# print(f"grey_color = {grey_color}")
# print(f"red_color = {red_color}")
# print(f"black_color = {black_color}")