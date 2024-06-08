import random

names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']

scores_dict = {item: random.randint(1, 101) for item in names}
print(scores_dict)