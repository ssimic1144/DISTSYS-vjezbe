def func1(x):
    assert isinstance(x, list) and all([isinstance(i, str) for i in x])
    return {k:v[::-1] for k,v in enumerate(x)}

def func2(x,y):
    assert isinstance(x, dict) and isinstance(y, dict)
    assert all([isinstance(i,list) for _,i in x.items()]) and all([isinstance(i,list) for _,i in y.items()])
    assert (x.get("valute") and x.get("cijena")) and (y.get("valute") and y.get("cijena"))
    return [(a,b) for a,d,b,c in zip(x["cijena"],y["cijena"], x["valute"], y["valute"]) if (a==d) and (b==c)]

def func3(x):
    assert isinstance(x,list) and all([isinstance(y, dict) for y in x])
    c = {k for d in x for a,k in d.items() if a=="kategorija"}
    return {k:sum([v["ocjena"] for v in x if v["kategorija"] == k]) for d in x for _,k in d.items() if k in c}





print(func1(["Stol", "Stolica", "Krevet", "Fotelja"]))
print(func2({"valute":["GBP","USD","CZK","Error"], "cijena":[8.5,7.7,0.3,10.3]}, {"valute":["EUR","USD","CZK","Error"], "cijena":[7.5,7.7,0.3,5.5]}))
print(func3([{"naziv":"Burek","kategorija":"pite", "ocjena":1},{"naziv":"Ramsteak","kategorija":"steak", "ocjena":9},{"naziv":"Ribeye","kategorija":"steak", "ocjena":4},{"naziv":"Sirnica","kategorija":"pite", "ocjena":5}]))
