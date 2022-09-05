import pika
from typing import List
from threading import Thread
import queue_utils._common as _common


class QueueConsumer:

    def __init__(self, host: str, port: int, queues_name: List[str], callback):
        # create connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self.channel = self.connection.channel()
        self.queues_name = queues_name

        # create/receive exchange service
        # direct queue allow us to have multiple consumers and on specific queue
        self.channel.exchange_declare(
            exchange=_common.rabbitmq_exchange_name,
            exchange_type='direct'
        )

        # create/receive queue
        result = self.channel.queue_declare(
            queue='',  # empty string value -> queue name will be auto generated
            exclusive=True
        )
        autogenerated_queue_name = result.method.queue  # queue name is automatically generated by the API

        # bind the queue to the exchange service with routing keys as a filter (routing keys)
        # user given queue names, for us, are actually the routing key
        for routing_key in queues_name:
            self.channel.queue_bind(
                exchange=_common.rabbitmq_exchange_name,
                queue=autogenerated_queue_name,  # automatically generated by the API
                routing_key=routing_key  # queue names given by the user are used as routing key
            )

        def incoming_message_callback(ch, method, properties, body):
            queue_name = method.routing_key
            message = body
            callback(queue_name, message)
            # print(" [x] %r:%r" % (method.routing_key, body))

        # register a callback for incoming messages
        self.channel.basic_consume(
            queue=autogenerated_queue_name,
            on_message_callback=incoming_message_callback,
            auto_ack=True
        )

        # start work
        self.callback_thread = Thread(target=self.channel.start_consuming)
        self.callback_thread.start()

    def __del__(self):
        self.connection.close()
