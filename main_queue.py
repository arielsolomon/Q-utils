from queue_utils.publisher import QueuePublisher
from queue_utils.consumer import QueueConsumer
import glob
import os

def callback(queue_name: str, message: bytes):
    print(f'queue name: {queue_name}, message: {message}')
img_root = '/home/user1/ariel/Signal/Sat_proj/data/22dB_05_04_22/images/test1'
img_list = glob.glob(os.path.join(img_root,'*.png'))

# Open single object of each and they connect via callback to the open docker

consumer = QueueConsumer(host='localhost', port=5672, queues_name=['image'], callback=callback)
publisher = QueuePublisher('localhost', 5672, "image")

for img in img_list:
    publisher.push_message(img)

import time
time.sleep(5)
