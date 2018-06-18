from .base import BaseMessage


class RequestAddrChangeMessage(BaseMessage):

    _type = BaseMessage.RequestAddressChange

    def __init__(self, sender, receiver, term, data):
        BaseMessage.__init__(self, sender, receiver, term, data)
