# http://www.usaco.org/index.php?page=viewproblem2&cpid=1205

import random
N = int(input(""))  # Number of words
letter_list = []
cl2 = []
for g in range(4):
    check_list = []
    point = 0
    a = input("")  # Block
    letter_list.append(a)
# This all works
word_list = []
for g in range(N):
    a = input("")
    word_list.append(a.upper())


def check(word, blocks):
    c = 0
    b = blocks.copy()
    for a in range(len(word)):
        for g in range(len(b)):
            if word[a] in b[g]:
                b.pop(g)
                c += 1
                break
        if c == len(word):
            return "YES"
    return "NO"


Ans = []
counter = 0
for h in range(58):
    random.shuffle(letter_list)
    for g in range(N):
        c = check(word_list[g], letter_list)
        if counter > N - 1:
            if Ans[g] == "NO" and c == "YES":
                Ans[g] = "YES"
        else:
            Ans.append(c)
        counter += 1
for g in range(N):
    print(Ans[g])
