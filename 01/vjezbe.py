import numpy as np

prva_varijabla = 1

print(prva_varijabla)

druga_varijabla = "Jedan"

print(druga_varijabla)

lista = list()

print(lista)

lista = []

print(lista)

lista.append(4)

lista = np.arange(20)

print(lista)

print([x for x in range(20)])

print([x for x in range(20) if x%2==0])
print([x if x%2==0 else -1 for x in range(20)])

r = []
for x in range(20):
    if x%2==0:
        r.append(x)
    else:
        r.append(-1)

print(r)

dictionary = dict()

print(dictionary)

d = {"kljuc":"vrijednost"}

d["jedan"] = 1

print(d)


t = ((1,2,3),23,"jedan")

print(t)

s = {1,23,5,4,1}

print(s)

lista = [x for x in range(19)]

d2 = {k:v if v%3==0 else 0 for k,v in enumerate(lista) }

print(d2)
d2 = {}
for x,y in enumerate(lista):
    if y%3==0:
        d2[x] = y
    else:
        d2[x] = 0

print(d2)

def func1(x):
    """
    x -> int
    """
    return x/2,x/3

print(func1(44))

x, y = func1(55)

print(x)
print(y)

for k,v in d2.items():
    print(k)
    print(v)

x = [(k,v) for k,v in d2.items()]

print(x)

def f1(x):
    """
    if isinstance(x,list) == False:
        print("not")
    assert isinstance(x, list)
    """
    return [y if y%4==0 else round(y**0.5,2)for y in x]

def f2(x,y):
    return {k:v  for k,v in zip(x,y) if len(x) == len(y)}


print(f1([213,14,12,6543,232]))


print(f2([1,2,3], [4,3,2]))
print(f2([1,3], [4,3,2]))

def f3(x):
    return {y for d in x for _,y in d.items()} 

print(f3([{"ip":"192.168.3.1"}, {"ip":"10.0.0.0"}, {"ip":"127.0.0.0"},{'ip':'192.168.3.1'}]))
