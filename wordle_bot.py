import pandas as pd
df=pd.read_csv('./wordle.csv')
df=df.to_numpy()
universe=[df[i][0] for i in range(len(df))]
# universe done
### preprocess universe to trie..... (keep to last)
#
#
#
#
# WALTZ VIBEX CHUNK FJORD GYMPS
# input processing
words=["WALTZ" ,"VIBEX", "CHUNK", "FJORD", "GYMPS"]
inputs = list(map(str ,input("WALTZ VIBEX CHUNK FJORD GYMPS gives (each word represent as b,g,y; EX: bbgyb, ..): ").strip().split()))[:5]
assert(sum([len(inputs[i])==5 for i in range(5)])==5)




possible=set({})
for i in range(5):
    for j in range(5):
        if inputs[i][j]=='y' or inputs[i][j]=='g':
            possible.add(words[i][j])

lists=[list(possible),list(possible),list(possible),list(possible),list(possible)]

for j in range(5):
    for i in range(5):
        if inputs[i][j]=='g':
            lists[j]=[words[i][j]]
            break
        elif inputs[i][j]=='y':
            lists[j].pop(lists[j].index(words[i][j]))

possible_words=[]
for q in lists[0]:
    for w in lists[1]:
        for e in lists[2]:
            for r in lists[3]:
                for t in lists[4]:
                    s=q+w+e+r+t
                    if s.lower() in universe:
                        possible_words.append(s)
print(possible_words)
#  bbbgb bgbby bybbb bbbbb bbbby