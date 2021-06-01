from aiohttp import web
import aiohttp_cors
import logging
import socketio

app = web.Application()
sio = socketio.AsyncServer(cors_allowed_origins='*')
sio.attach(app)
logging.basicConfig(level=logging.DEBUG)
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
        allow_credentials=True,
        expose_headers="*",
        allow_headers="*",
    )
})


@sio.event
async def question(sid, data):
    logging.info('question event by ', sid)


@sio.event
def connect(sid, environ, auth):
    logging.info('connect ', sid)


@sio.event
def disconnect(sid):
    logging.info('disconnect ', sid)


async def index(request):
    logging.info('what is up')
    return web.Response(text='async_server', content_type='text/html')


cors.add(app.router.add_get('/*', index))


if __name__ == '__main__':
    web.run_app(app)
