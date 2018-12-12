from functools import partial

import abc

# adapted from prouhard
class MethodDecorator(metaclass=abc.ABCMeta):
    def __init__(self, *args, **kwargs):
        self.method = None
        self.args = []
        if args:
            self.method, *self.args = args
        self.kwargs = kwargs
        self._is_staticmethod = None

    def __call__(self, method):
        self.args = [self.method, *self.args]
        self.method = method
        return self

    def __get__(self, obj, objtype=None):
        self._is_staticmethod = obj == None
        if self._is_staticmethod:
            return self.wrapper
        return partial(self.wrapper, obj)

    @property
    def is_staticmethod(self):
        return self._is_staticmethod

    @abc.abstractmethod
    def wrapper(self, *args, **kwargs):
        pass


class if_None(MethodDecorator):
    def wrapper(self, *args, **kwargs):
        value = self.kwargs.get('value')
        if value:
            return value
        return self.method(*args, **kwargs)