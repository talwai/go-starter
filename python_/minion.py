import os
import zmq

MASTER_IP = os.environ.get('MASTER_IP', 'localhost')
MASTER_PORT = os.environ.get('MASTER_PORT', 4550)


ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)
socket.connect('tcp://{0}:{1}'.format(MASTER_IP, MASTER_PORT))

topic_filter = bytes('SPORTS', 'utf-8')
socket.setsockopt(zmq.SUBSCRIBE, topic_filter)

while True:
    s = socket.recv()
    print(s)
