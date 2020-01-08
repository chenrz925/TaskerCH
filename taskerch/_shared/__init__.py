from taskerch._shared._base import Shared
from taskerch.task import Namespace


class SharedBuilder(object):
    _support_backends = {
        'dict': {
            'module': 'taskerch._shared._dict',
            'class': 'DictShared',
            'require': []
        },
    }

    def __init__(self, config: Namespace=None):
        pass

