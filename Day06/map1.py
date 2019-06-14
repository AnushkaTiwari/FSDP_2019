# Code Challenge : Rewrite using map and lambda

""" import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)"""


import random

names=['Mary','Isla','Sam']
code_names=['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']       
result=map(lambda names :random.choice(code_names),names )
print(list(result))