import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/")
async def get_hendler(request):
    try:
        tasks = []
        async with aiohttp.ClientSession() as session:
            for _ in range(5):
                tasks.append(asyncio.create_task(session.get("https://google.com")))
            res = await asyncio.gather(*tasks)
            res = [len(await x.text()) for x in res]
            print(res)
        return web.json_response({"status":"ok"}, status=200)
    except Exception as e:
        return web.json_response({"status":"failed","message":str(e)}, status=500)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)

