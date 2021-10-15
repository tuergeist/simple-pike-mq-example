import time
from datetime import datetime

from channel_setup import get_mq_channel

channel = get_mq_channel()

queue = 'telegram'
channel.queue_declare(queue)



while True:
    msg = f"It's now {datetime.now()}"
    channel.basic_publish('', queue, msg)
    time.sleep(2)
