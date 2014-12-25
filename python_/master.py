import os
import zmq
from random import choice

MASTER_PORT = os.environ.get('MASTER_PORT', 4550)
POSSIBLE_TOPICS = ['PING', 'CMD', 'SPORTS']

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)

socket.bind('tcp://*:{}'.format(MASTER_PORT))

while True:
    topic = choice(POSSIBLE_TOPICS)
    string = '{} kakkas'.format(topic)
    #print('Sending {}'.format(string))
    socket.send_string(string)
