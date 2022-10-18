def func1(x):
    assert all([isinstance(y, str) for y in x])
    return [y for y in x if len(y) > 4]

def func2(x,y):
    assert (isinstance(x, list) and isinstance(y, dict))
    assert len(x) == len(y)
    assert all([isinstance(y, int) for y in x])
    return {k:v if (v > 5 and v < 10) else -1 for k,v in zip(y,x)}

def func3(x):
    assert isinstance(x, list)
    assert all([isinstance(y,dict) for y in x])
    assert all([bool(y) if len(y.keys()) == 3 else False for y in x ])
    assert all([bool(y) if (y == "cijena") or (y == "naziv") or (y == "kolicina") else False for d in x for y in d.keys()])
    cijena = sum([j["cijena"]*j["kolicina"] for j in x])
    artikli = [i["naziv"] for i in x]
    return {"ukupno":{"artikli":artikli, "cijena":cijena}}
    

print(func1(["Pas", "Macka", "Stol"]))
print(func2([8,7,1], {1:2,2:1,3:2}))
print(func3([{"cijena":8,"naziv":"Kruh","kolicina":3}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}]))
