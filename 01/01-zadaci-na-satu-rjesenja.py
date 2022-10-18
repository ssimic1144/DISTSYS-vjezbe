def func1(x):
    return [y if y%4==0 else round(y**0.5,2) for y in x]

def func2(x,y):
    return {k:v for k,v in zip(x,y) if len(x) == len(y)}

def func3(x):
    return {y for d in x for _,y in d.items()}

def func4(x,y):
    assert len(x) == len(y)
    return [i if i==j else -1 for i,j in zip(x,y)]

def func5(x):
    return [{"id":i,"ime":j,"prezime":k} for i,j,k in sorted(x) if j[0] == k[0]]

def func6(x,y):
    assert type(x) == type(y)
    assert isinstance(x, list) or isinstance(x, dict)
    if isinstance(x,list):
        return [*x,*y] 
    else:
        return {**x,**y}

print("Prvi : ", func1([213,14,12,6543,232]))
print("Drugi : ", func2([1,2,3],[4,3,2]))
print("Drugi : ", func2([1,3],[4,3,2]))
print("Treci : ", func3([{"ip":"192.168.3.1"}, {"ip":"10.0.0.0"}, {"ip":"127.0.0.0"}, {"ip":"192.168.3.1"}]))
print("Cetvrti : ",func4([1,2,3,4,5],[2,2,4,4,5]))
#print("Cetvrti : ",func4([2,3,4,5],[2,2,4,4,5]))
print("Peti : ", func5([(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]))
print("Sesti : ", func6({1:2,3:2},{5:2,4:1}))
print("Sesti : ", func6([1,2,1,2],[3,2]))
#print("Sesti : ", func6([1,3],{5:2,4:1}))
#print("Sesti : ", func6({1,2},{3,2}))
