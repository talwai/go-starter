import os
import zmq

import constants
from message import ZMQMessage

MASTER_IP = os.environ.get('MASTER_IP', 'localhost')
MASTER_PORT = os.environ.get('MASTER_PORT', 4550)

SUBSCRIBE_TOPICS = [constants.PING_TOPIC, constants.COMMAND_TOPIC]

ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)

for topic in SUBSCRIBE_TOPICS:
    socket.setsockopt(zmq.SUBSCRIBE, topic)

socket.connect('tcp://{0}:{1}'.format(MASTER_IP, MASTER_PORT))


while True:
    received_msg = socket.recv()
    _parsed = ZMQMessage.parse_msg(received_msg)
    msg_class = ZMQMessage.get_message_class(_parsed)

    msg = msg_class(**_parsed)
    msg.process(with_socket=socket)
