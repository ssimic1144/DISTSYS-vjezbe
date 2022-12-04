import aiosqlite
import aiohttp
import asyncio
from aiohttp import web


routes = web.RouteTableDef()

temp_users = []
temp_jokes = []

@routes.post("/storeData")
async def store_data(request):
    global temp_users, temp_jokes
    json_data = await request.json()
    user_data = []
    joke_data = []
    try:
        user_data.append(json_data["data"]["user"])
        temp_users += user_data
    except KeyError:
        joke_data.append(json_data["data"]["joke"])
        temp_jokes += joke_data
    #print("User: ", user_data)
    #print("Joke: ", joke_data)
    if len(user_data) > 0:
        if len(temp_jokes) > 0 and len(temp_users) > 0:
            db_input = {**user_data[0],**temp_jokes[0]}

            async with aiosqlite.connect("06/data-store.db") as db:
                await db.execute("INSERT INTO UsersJoke (name,city,username,setup,punchline) VALUES (?,?,?,?,?)", (db_input["name"],db_input["city"],db_input["username"],db_input["setup"],db_input["punchline"]))
                await db.commit()

            #print("Temp j :", temp_jokes)
            temp_jokes = temp_jokes[1:]
            #print("user data :", user_data)
            #print("temp users :", temp_users)
            temp_users = temp_users[1:]
            #print("temp users :", temp_users)

            async with aiosqlite.connect("06/data-store.db") as db:
                async with db.execute("SELECT * FROM UsersJoke") as cur:
                    #print("Every row in DB : ", await cur.fetchall())
                    result = len(await cur.fetchall())
            message = {"status":"ok","data":{"numberOfRowsInTable":result}}

            return web.json_response(message, status=200)
        else:
            message = {"status":"Failed","message":"Joke not present"}
            return web.json_response(message, status=400)
    else:
        if len(temp_jokes) > 0 and len(temp_users) > 0:
            db_input = {**joke_data[0],**temp_users[0]}

            async with aiosqlite.connect("06/data-store.db") as db:
                await db.execute("INSERT INTO UsersJoke (name,city,username,setup,punchline) VALUES (?,?,?,?,?)", (db_input["name"],db_input["city"],db_input["username"],db_input["setup"],db_input["punchline"]))
                await db.commit()

            temp_users = temp_users[1:]
            #print("Joke data :", joke_data)
            temp_jokes = temp_jokes[1:]
            #print("Temp j after pop :", temp_jokes)

            async with aiosqlite.connect("06/data-store.db") as db:
                async with db.execute("SELECT * FROM UsersJoke") as cur:
                    result = len(await cur.fetchall())
            message = {"status":"ok","data":{"numberOfRowsInTable":result}}

            return web.json_response(message, status=200)
        else:
            message = {"status":"Failed","message":"User not present"}
            return web.json_response(message, status=400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8083)
