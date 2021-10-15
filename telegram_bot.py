"""Basic message consumer example"""
import logging

from channel_setup import get_mq_channel

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def on_message(chan, method_frame, header_frame, body, userdata=None):
    """Called when a message is received. Log message and ack it."""
    LOGGER.info('Delivery properties: %s, message metadata: %s', method_frame, header_frame)
    LOGGER.info('message body: %s', body)
    chan.basic_ack(delivery_tag=method_frame.delivery_tag)


def main():
    """Main method."""
    queue = 'telegram'
    channel = get_mq_channel()

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue, on_message_callback=on_message)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()


if __name__ == '__main__':
    main()
