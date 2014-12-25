import subprocess
import constants

def _request_global_socket():
    pass

def _get_next_id():
    return 1

class ZMQMessage(object):
    def __init__(self, id, topic, content):
        self.id = id
        self.topic = topic
        self.content = content

    @staticmethod
    def parse_msg(msg_object):
        # Msg is either plaintext string, JSON string, or pickled Python object
        # For now, assume plain string
        topic, content = msg.split(' ')
        return {
                'id': _get_next_id()
                'topic': topic,
                'content': content
        }

    @staticmethod
    def get_message_class(parsed_msg):
        topic = parsed_msg.get('topic')
        if topic == 'CMD':
            return CMDMessage
        elif topic == 'PING':
            return PINGMessage
        else:
            raise NotImplementedError


    def process(self):
        raise NotImplementedError

class PINGMessage(ZMQMessage):
    def process(self, with_socket=None):
        socket = with_socket if with_socket else _request_global_socket()
        socket.send(constants.PONG_MSG)

class CMDMessage(ZMQMessage):
    def process(self, with_socket=None):
        socket = with_socket if with_socket else _request_global_socket()
        cmd_str = self.content.split(' ')
        ret = subprocess.call(cmd_str)
        socket.send(ret.encode())
