from enum import Enum


class ResponseStrings(Enum):
    '''This enum class is used to create responses in views methods.'''
    FAILED = 'failed'
    SUCCESS = 'success'

    STATUS = 'status'
    MESSAGE = 'msg'
    TOKEN = 'token'
    NAME = 'name'

class ResponseMessages(Enum):
    '''This enum stores ready responses'''
    INVALID_TOKEN = {
            ResponseStrings.STATUS.value: ResponseStrings.FAILED.value,
            ResponseStrings.MESSAGE.value: "Invalid token"
        }