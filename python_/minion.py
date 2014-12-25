import os
import zmq

MASTER_IP = os.environ.get('MASTER_IP', 'localhost')
MASTER_PORT = os.environ.get('MASTER_PORT', 4550)

SUBSCRIBE_TOPICS = ['PING', 'CMD']

ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)
topic_filters = [ bytes(t, 'utf-8') for t in SUBSCRIBE_TOPICS ]
for tf in topic_filters:
    socket.setsockopt(zmq.SUBSCRIBE, tf)

socket.connect('tcp://{0}:{1}'.format(MASTER_IP, MASTER_PORT))


while True:
    s = socket.recv()
    print(s)
