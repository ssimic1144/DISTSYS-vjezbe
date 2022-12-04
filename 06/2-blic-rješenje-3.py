import aiohttp
import asyncio
from aiohttp import web


routes = web.RouteTableDef()

@routes.post("/filterJoke")
async def filter_joke(request):
    try:
        json_data = await request.json()
        joke ={}
        joke["setup"] = json_data["setup"]
        joke["punchline"] = json_data["punchline"]
        result = {"data":{"joke":joke}}
        #print(result)
        async with aiohttp.ClientSession() as session:
            message = await asyncio.create_task(session.post("http://0.0.0.0:8083/storeData", json=result))
            message = await message.json()
        return web.json_response({"messages":message}, status=200)
    except Exception as e:
        return web.json_response({"serviceNumber":3,"messages":str(e)}, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)
