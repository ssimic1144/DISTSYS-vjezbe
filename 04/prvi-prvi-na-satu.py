import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getFact")
async def get_fact(req):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(20):
            tasks.append(asyncio.create_task(session.get("https://catfact.ninja/fact")))
        res = await asyncio.gather(*tasks)
        res = [await x.json() for x in res]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(len(res)):
            tasks.append(asyncio.create_task(session.post("http://0.0.0.0:8081/saveFact",json=res[i])))
        res = await asyncio.gather(*tasks)
        res = [await x.json() for x in res]
    return web.json_response({"status":"ok", "messages":res}, status=200)




app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
