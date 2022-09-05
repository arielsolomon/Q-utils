from queue_utils.publisher import QueuePublisher
from queue_utils.consumer import QueueConsumer
import glob
import os

def callback(queue_name: str, message: bytes):
    print(f'queue name: {queue_name}, message: {message}')
img_root = '/Data/Signals/Sat_proj/data/05_04_22dB/images/train'
img_list = glob.glob(os.path.join(img_root,'*.png'))

consumer = QueueConsumer(host='localhost', port=5672, queues_name=['image'], callback=callback)
publisher = QueuePublisher('localhost', 5672, "image")
publisher.push_message(b'hello world 1')
publisher.push_message(b'hello world 2')
publisher.push_message(b'hello world 3')

import time
time.sleep(5)
