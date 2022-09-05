import pika
import queue_utils._common as _common


class QueuePublisher:

    def __init__(self, host: str, port: int, queue_name: str):
        # create connection
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=port))
        self.channel = self.connection.channel()
        self.queue_name = queue_name

        # create/receive exchange service
        # direct queue allow us to have multiple consumers and on specific queue
        xxx = self.channel.exchange_declare(exchange=_common.rabbitmq_exchange_name, exchange_type='direct')
        print(xxx)

    def __del__(self):
        self.connection.close()

    def push_message(self, message_body: bytes):
        xxx = self.channel.basic_publish(
            exchange=_common.rabbitmq_exchange_name,
            routing_key=self.queue_name,  # we use the user's 'queue name' as the routing key to filter messages
                                          # the consumer will use this routing key to receive filtered messages
            body=message_body
        )
        print(xxx)

