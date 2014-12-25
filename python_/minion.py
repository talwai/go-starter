import zmq

MASTER_PORT = 4550
ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)
socket.connect('tcp://localhost:4550')

topic_filter = bytes('SPORTS', 'utf-8')
socket.setsockopt(zmq.SUBSCRIBE, topic_filter)

while True:
    s = socket.recv()
    print(s)
