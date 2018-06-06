__author__ = 'Ian Han'

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from aiohttp import web

def index(request):
    return web.Response(body='<h1>Awesome</h1>')

#@asyncio.coroutine
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
#     srv = yield from loop.create_server(app.make_handler(), '127.0.0.1',8000)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1',8000)
    logging.info('server started at http://127.0.0.1:8000')
    return srv
    
loop =asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
