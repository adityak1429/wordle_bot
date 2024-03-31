import pandas as pd
import numpy as np
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy
df=pd.read_csv('./wordle.csv')
df=df.to_numpy()
universe=([df[i][0] for i in range(len(df))])
# universe done
### preprocess universe to trie..... (keep to last)
#
#
#
#
# WALTZ VIBEX CHUNK FJORD GYMPS
# input processing
words=[]
inputs=[]
words=["STARE","CLOUD","PINKY"]
inputs.append(str(input()))#"what is its code:"
inputs.append(str(input()))#"what is its code:"
inputs.append(str(input()))#"what is its code:"

#words=["WALTZ" ,"VIBEX", "CHUNK", "FJORD", "GYMPS"]
start=0
yellows=set({})
while True:

    num=len(words)
    print("RUNNING")
    possible=set({'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'})

    for i in range(num):
        for j in range(5):
            if inputs[i][j]=='b':
                possible.discard(words[i][j])
    
    lists=[set(possible),set(possible),set(possible),set(possible),set(possible)]

    for j in range(5):
        for i in range(start,num):
            if inputs[i][j]=='g':
                lists[j]=set([words[i][j]])
            elif inputs[i][j]=='y':
                lists[j].discard(words[i][j])
                yellows.add(words[i][j])

    possible_words=[]
    for q in lists[0]:
        for w in lists[1]:
            for e in lists[2]:
                for r in lists[3]:
                    for t in lists[4]:
                        s=q+w+e+r+t
                        if s.lower() in universe:
                            x=True
                            for i in yellows:
                                if i not in s:
                                    x=False
                            if x:
                                possible_words.append(s)
    print(possible_words)
    print("DONE")
    universe=[]
    for i in possible_words:
        universe.append(i.lower())
    if len(possible_words)>1:
        if 1:#1:(int(input("do you wish to continue [1/0]")))!=0:#
            start=num
            words.append(str(input()).upper())#"which word u want to add:"
            inputs.append(str(input()).lower())#"what is its code:"
        else:
            break
    else:
        break

#  bbbgb bgbby bybbb bbbbb bbbby
