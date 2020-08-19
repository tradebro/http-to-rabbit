from os import environ
from sanic.log import logger
from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, text
import asyncio
import aio_pika
import ujson

AMQP_CONN_STRING = environ.get('AMQP_CONN_STRING')
AMQP_QUEUE = environ.get('AMQP_QUEUE')
AMQP_ORDERS_EXCHANGE = environ.get('AMQP_ORDERS_EXCHANGE')


async def webhook_handler(request: Request) -> HTTPResponse:
    conn: aio_pika.Connection = await aio_pika.connect(url=AMQP_CONN_STRING,
                                                       loop=asyncio.get_event_loop())

    channel = await conn.channel()
    await channel.declare_queue(name=AMQP_QUEUE,
                                auto_delete=True)
    exchange = channel.declare_exchange(name=AMQP_ORDERS_EXCHANGE,
                                        type=aio_pika.ExchangeType.FANOUT)

    amqp_message = aio_pika.Message(body=ujson.dumps(request.json).encode())
    await exchange.publish(message=amqp_message,
                           routing_key=AMQP_QUEUE)
    logger.debug('Message is published to queue')

    return text('ok')


def create_app() -> Sanic:
    app = Sanic('Rabbit to HTTP')
    app.add_route(webhook_handler, '/message', methods=['POST'])

    return app
