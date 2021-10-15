import logging

import pika


def get_mq_channel():
    HOST = 'localhost'
    PORT = 5672
    CREDS = pika.PlainCredentials('user', 'password')

    logging.basicConfig(level=logging.DEBUG)

    connection = pika.BlockingConnection(pika.ConnectionParameters(HOST, PORT, '/', CREDS))
    channel = connection.channel()
    return channel