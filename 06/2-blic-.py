import aiohttp
from aiohttp import web
import asyncio

routes = web.RouteTableDef()

@routes.get("/getJokes")
async def get_activity(request):
    async with aiohttp.ClientSession() as session:
        for _ in range(6):
            for __ in range(2):
                tasks = []
                tasks.append(
                    asyncio.create_task(session.get("https://randomuser.me/api/"))
                )
                user_data = await asyncio.gather(*tasks)
                user_data = [await x.json() for x in user_data]

                for _ in range(len(user_data)):
                    async with session.post("http://localhost:1/filterUser", json = user_data) as res:
                        response = await res.json()

                tasks = []
                tasks.append(
                    asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke"))
                )
                joke_data = await asyncio.gather(*tasks)
                joke_data = [await x.json() for x in joke_data]

                for _ in range(len(joke_data)):
                    async with session.post("http://localhost:2/filterJoke", json = joke_data) as res:
                        result = await res.json()

    return web.json_response({"resp": response, "resu": result})


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
