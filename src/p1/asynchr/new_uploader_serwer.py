import os.path
from asyncio import sleep
from random import randint

from aiohttp import web
from aiohttp.abc import BaseRequest
from aiohttp.web_middlewares import middleware
from faker import Faker

routes = web.RouteTableDef()

# pip install aiohttp

"""
query = req.match_info.get('query', '')  # for route-resolving, /{query}
query = req.rel_url.query['query']  # params; required; else .get('query','default')
"""


@routes.get('/')
async def hello(request):
    print('request received')
    return web.json_response({'comment': f'hello, x={12}!'})

@middleware
async def middleware(request, handler):
    # "opakowuje" każdy request... można tu zrobić try... expect...
    print(f'request: {request}')
    resp = await handler(request)
    print(f'response: {resp.status}')
    return resp

@routes.get('/serve')
async def serve_file(request):
    filename = request.rel_url.query.get('filename', '')
    path = f'images/{filename}'
    if '..' in filename or '/' in filename or "\\" in filename or not os.path.isfile(path):
        raise RuntimeError('Invalid filename')
    return web.FileResponse(f'images/{filename}')

@routes.post('/upload')
async def accept_file(req: BaseRequest):
    """
    Funkcja przyjmująca upload pliku.
    """
    # https://docs.aiohttp.org/en/stable/web_quickstart.html#file-uploads
    print('file upload request hit...')
    reader = await req.multipart()

    # field = await reader.next()
    # name = await field.read(decode=True)

    field = await reader.next()
    assert field.name == 'file'
    print(f'read field object: {field}')
    filename = field.filename
    # Cannot rely on Content-Length if transfer is chunked.
    print(f'filename:{filename}')
    filename = 'images/' + filename
    size = 0
    with open(filename, 'wb') as f:
        file_as_bytes = b''
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            print(type(chunk))
            if not chunk:
                break
            size += len(chunk)
            file_as_bytes += chunk
            # f.write(chunk)
        f.write(file_as_bytes)

    return web.json_response({'name': filename, 'size': size})



async def starter():
    """
    Starter / app factory, czyli miejsce gdzie można inicjalizować asynchronicze konstrukty.
    """
    await sleep(0.2)
    print('app is starting..')
    # await database.connect()
    return app


app = web.Application(middlewares=[middleware])
app.add_routes(routes)
web.run_app(starter(), port=8888)  # ewentu
