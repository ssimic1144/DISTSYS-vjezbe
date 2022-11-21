import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

temp = [{
    "ime":"Stol"
    },
    {
        "ime":"Laptop" }]

@routes.get("/")
async def get_hendler(request):
    return web.json_response({"status":"ok"}, status=200)

@routes.get("/artikl")
async def get_artikl(request):
    """
    q = request.query
    print(type(q))
    print(q)
    q = q.get("ime")
    print(q)
    """
    q = request.query.get("ime")
    res = [d for d in temp if d.get("ime") == q]
    return web.json_response({"status":"ok", "data":res}, status=200)

@routes.post("/artikl")
async def post_artikl(request):
    json_data = await request.json()
    print(json_data)
    print(type(json_data))
    temp.append(json_data)
    return web.json_response({"status":"ok"}, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
