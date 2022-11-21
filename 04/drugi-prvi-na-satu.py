import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

temp = []

@routes.post("/saveFact")
async def save_fact(request):
    try:
        json_data = await request.json()
        print(json_data)
        if json_data.get("length") > 100:
            temp.append(json_data)
            return web.json_response({"Message":json_data.get("fact")}, status=200)
        else:
            return web.json_response({"Failed":"Prekratko"}, status=400)
    except Exception as e:
            return web.json_response({"Failed":str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)
