import aiohttp
import asyncio
from aiohttp import web


routes = web.RouteTableDef()

@routes.post("/filterUser")
async def filter_user(request):
    try:
        json_data = await request.json()
        #print(json_data)
        user = {}
        data = json_data["results"][0]
        user["name"] = data["name"]["first"] + " " + data["name"]["last"]
        user["city"] = data["location"]["city"]
        user["username"] = data["login"]["username"]
        result = {"data":{"user":user}}
        async with aiohttp.ClientSession() as session:
            message = await asyncio.create_task(session.post("http://0.0.0.0:8083/storeData", json=result))
            message = await message.json()
        return web.json_response({"messages":message}, status=200)
    except Exception as e:
        return web.json_response({"serviceNumber":2,"messages":str(e)}, status=200)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)
