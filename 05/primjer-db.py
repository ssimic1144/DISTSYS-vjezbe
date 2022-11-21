import aiosqlite
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/artikli")
async def get_artikli_db(request):
    res = []
    async with aiosqlite.connect("05/test.db") as db:
        async with db.execute("SELECT * FROM artikl") as cur:
            async for row in cur:
                res.append(row)

            await db.commit()

    return web.json_response({"status":"ok", "data":res}, status=200)

    
@routes.post("/artikl")
async def post_artikl_db(request):
    req = await request.json()
    async with aiosqlite.connect("05/test.db") as db:
        await db.execute("INSERT INTO artikl (ime,cijena) VALUES (?,?)", (req["ime"],req["cijena"]))
        await db.commit()

    return web.json_response({"status":"ok" }, status=200)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app)
