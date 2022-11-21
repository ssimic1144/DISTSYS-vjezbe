import os
import asyncio


async def afunc1(list_of_filenames):
    await asyncio.sleep(0.2)

    print("Async Working")
    
    results = [os.path.getsize(filename) for filename in list_of_filenames]

    print(results)

    return results
    
def fun2():
    get_list_of_files = os.listdir()
    print(get_list_of_files)
    for filename in get_list_of_files:
        if "datoteka" in filename :
            with open(filename, "w") as file:
                for number in range(10000):
                    file.write(str(number)+ "\n")

async def main():
    filenames = list()
    for i in range(3):
        filename = "datoteka"+str(i)
        print(filename)

        # Write mode
        with open(filename,"w") as file:
            pass

        filenames.append(filename)

    #Create async function
    list_of_filenames = asyncio.create_task(afunc1(filenames))

    fun2()

    await asyncio.gather(list_of_filenames)



if __name__=="__main__":
    asyncio.run(main())
