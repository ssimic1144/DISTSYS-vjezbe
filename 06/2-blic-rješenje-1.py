import aiohttp
import asyncio
from aiohttp import web


routes = web.RouteTableDef()

#
@routes.get("/getJokes")
async def get_jokes(request):
    jokes_tasks = []
    users_tasks = []
    final_results = []
    async with aiohttp.ClientSession() as session:
        for _ in range(4):
            users_tasks.append(asyncio.create_task(session.get("https://randomuser.me/api/")))
            jokes_tasks.append(asyncio.create_task(session.get("https://official-joke-api.appspot.com/random_joke")))
        res = users_tasks + jokes_tasks
        final_results = await asyncio.gather(*res)
        final_results = [await x.json() for x in final_results]
    jokes_tasks = []
    users_tasks = []
    async with aiohttp.ClientSession() as session:
        half = int(len(final_results)/2)
        for i in range(half):
            users_tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8081/filterUser",json=final_results[i])))
            jokes_tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8082/filterJoke",json=final_results[half+i])))
        final_results = await asyncio.gather(*[*users_tasks,*jokes_tasks])
        final_results = [await x.json() for x in final_results]
    return web.json_response({"results":final_results}, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
