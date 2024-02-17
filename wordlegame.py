import pandas as pd
import random
df=pd.read_csv('./wordle.csv')
df=df.to_numpy()
universe=[df[i][0] for i in range(len(df))]
ourword=random.choice(universe)
for i in range(6):
    query=str(input()).lower()
    if query=="suicide":
        break
    if query==ourword:
        print(f'{query} is found')
        break
    for j in range(5):
        if query[j]==ourword[j]:
            print('g', end='')
        elif query[j] in ourword:
            print('y', end='')
        else:
            print('b', end='')
    print()
print(f"the word is {query}")