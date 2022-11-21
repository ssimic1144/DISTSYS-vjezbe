import asyncio
import numpy as np

#Prvi
"""
async def fun1():
    return [{"artikl":v} for v in ["Kava","Voda"]]

async def fun2(x):
    assert isinstance(x, list) and all([isinstance(d, dict)] for d in x)
    return [{**d, **{"cijena":np.random.randint(1,10)}} for d in x]

async def main():
    artikli = await fun1()
    final = await fun2(artikli)
    print(final)
"""

#Drugi
async def func1(x):
    assert isinstance(x,list)
    return [{"korisnik":e,"id":i} for i,e in enumerate(x)]


async def func2():
    for x in range(10):
        await asyncio.sleep(0.01)
        print(x)

async def func3(x):
    assert isinstance(x, list) and all([isinstance(d,dict) for d in x])
    assert all([d.get("korisnik") for d in x]) 
    assert all([True if d.get("id",None) is not None else False for d in x ]) 
    await asyncio.sleep(0.05)
    return [(d.get("korisnik"),d.get("id"), len(d.get("korisnik"))) for d in x]


async def main():
    imena = ["Ivan","Pero","Ana"] 
    mid_res = await func1(imena)
    asyncio.create_task(func2())
    final = await func3(mid_res)
    print(final) 

if __name__=="__main__":
    asyncio.run(main())
