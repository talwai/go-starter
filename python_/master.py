import zmq

MASTER_PORT = 4550

ctx = zmq.Context()
socket = ctx.socket(zmq.PUB)

socket.bind('tcp://*:{}'.format(MASTER_PORT))

while True:
    string = 'SPORTS abcd'
    #print('Sending {}'.format(string))
    socket.send_string(string)
