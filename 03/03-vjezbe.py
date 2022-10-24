import asyncio
import time

async def fun1():
    for x in range(10):
        await asyncio.sleep(0.2)
        print("Prva :", x)
    return ["Jedan"]

async def fun2():
    for x in range(20):
        await asyncio.sleep(0.1)
        print("Druga : ", x+10)
    return ["Dva"]

def fun3():
    for x in range(5):
        time.sleep(0.4)
        print("Treca : ", x-123)

async def main():
    var1 = asyncio.create_task(fun1())
    var2 = asyncio.create_task(fun1())
    var3 = asyncio.create_task(fun1())
    fun3()
    await fun2()
    res = await asyncio.gather(var1,var2,var3)
    print(res)

if __name__ == "__main__":
    asyncio.run(main())

