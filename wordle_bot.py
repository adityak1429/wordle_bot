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
# words=["STARE","CLOUD","PINKY"]
while True:
    words=["WALTZ" ,"VIBEX", "CHUNK", "FJORD", "GYMPS"]
    for i in words:
        print(i)
    num=len(words)
    inputs = list(map(str ,input().strip().split()))[:num]#"WALTZ VIBEX CHUNK FJORD GYMPS gives (each word represent as b,g,y; EX: bbgyb, ..): "
    assert(sum([len(inputs[i])==5 for i in range(num)])==num)

    possible=set({'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'})

    for i in range(num):
        for j in range(5):
            if inputs[i][j]=='b':
                possible.remove(words[i][j])

    lists=[list(possible),list(possible),list(possible),list(possible),list(possible)]


    for j in range(5):
        for i in range(num):
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
    print(possible_words[0])
    if len(possible_words)>1:
        if int(input()):#"do you wish to continue [1/0]"
            words.append(str(input()))#"which word u want to add:"
            inputs.append(str(input()))#"what is its code:"
        else:
            break
    else:
        break

while True:
    print(input())

#  bbbgb bgbby bybbb bbbbb bbbby