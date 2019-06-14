# Code Challenge : Rewrite  code using map

 """ names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)

"""
names=['Mary','Isla','Sam']


def assign(names):
    return hash(names[i])

result=map(assign,names)
print(list(result))